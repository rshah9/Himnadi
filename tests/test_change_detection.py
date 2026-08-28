from datetime import date

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from change_detection import AreaObservation, check_for_alert
from config import MonitoredSite


def _site():
    return MonitoredSite(
        site_id="test-site",
        name="Test Site",
        description="unit test fixture",
        bbox=(0, 0, 1, 1),
        area_growth_alert_threshold_pct=15.0,
        baseline_window_days=30,
    )


def test_no_alert_when_no_history():
    site = _site()
    current = AreaObservation("test-site", date(2026, 8, 26), 1000.0, "sentinel-2")
    assert check_for_alert(site, current, []) is None


def test_alert_triggered_on_large_growth():
    site = _site()
    history = [
        AreaObservation("test-site", date(2026, 8, d), 1000.0, "sentinel-2")
        for d in range(1, 20)
    ]
    current = AreaObservation("test-site", date(2026, 8, 26), 1300.0, "sentinel-2")
    alert = check_for_alert(site, current, history)
    assert alert is not None
    assert alert.severity in ("warning", "critical")


def test_no_alert_on_small_change():
    site = _site()
    history = [
        AreaObservation("test-site", date(2026, 8, d), 1000.0, "sentinel-2")
        for d in range(1, 20)
    ]
    current = AreaObservation("test-site", date(2026, 8, 26), 1020.0, "sentinel-2")
    assert check_for_alert(site, current, history) is None
