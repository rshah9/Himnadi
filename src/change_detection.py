"""
Compare a site's current lake area against its historical baseline and
flag anomalies worth a human look.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from config import MonitoredSite


@dataclass
class AreaObservation:
    site_id: str
    observed_date: date
    area_m2: float
    source: str


@dataclass
class ChangeAlert:
    site_id: str
    observed_date: date
    current_area_m2: float
    baseline_area_m2: float
    pct_change: float
    severity: str  # "info" | "warning" | "critical"


def compute_baseline_area(
    history: list[AreaObservation], as_of: date, window_days: int
) -> float | None:
    """
    Average lake area over the baseline window ending just before `as_of`.
    Returns None if there isn't enough history yet.
    """
    window_start = as_of.toordinal() - window_days
    relevant = [
        obs
        for obs in history
        if window_start <= obs.observed_date.toordinal() < as_of.toordinal()
    ]
    if not relevant:
        return None
    return sum(o.area_m2 for o in relevant) / len(relevant)


def check_for_alert(
    site: MonitoredSite,
    current: AreaObservation,
    history: list[AreaObservation],
) -> ChangeAlert | None:
    """
    Compare the current observation to the site's baseline and return a
    ChangeAlert if the change exceeds the site's configured threshold.
    """
    baseline = compute_baseline_area(
        history, current.observed_date, site.baseline_window_days
    )
    if baseline is None or baseline == 0:
        return None

    pct_change = (current.area_m2 - baseline) / baseline * 100

    if pct_change < site.area_growth_alert_threshold_pct:
        return None

    severity = "warning"
    if pct_change >= site.area_growth_alert_threshold_pct * 2:
        severity = "critical"

    return ChangeAlert(
        site_id=site.site_id,
        observed_date=current.observed_date,
        current_area_m2=current.area_m2,
        baseline_area_m2=baseline,
        pct_change=pct_change,
        severity=severity,
    )
