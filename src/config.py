"""
Configuration for monitored sites.

Each site is a region of interest (a glacial lake, glacier front, or
river reach) defined by a bounding box, plus metadata and alert thresholds.

Coordinates below are illustrative placeholders — replace with verified
coordinates from ICIMOD's glacial lake inventory or your own survey before
using this for anything real.
"""

from dataclasses import dataclass, field


@dataclass
class MonitoredSite:
    site_id: str
    name: str
    description: str
    # Bounding box: (min_lon, min_lat, max_lon, max_lat)
    bbox: tuple[float, float, float, float]
    # Percent area growth over baseline that should trigger an alert
    area_growth_alert_threshold_pct: float = 15.0
    # How far back to look for the baseline, in days
    baseline_window_days: int = 365
    tags: list[str] = field(default_factory=list)


# Placeholder example sites — REPLACE with real, verified coordinates.
MONITORED_SITES: list[MonitoredSite] = [
    MonitoredSite(
        site_id="example-rasuwa-01",
        name="Example site — Rasuwa district",
        description=(
            "Placeholder entry near the Aug 2026 event area. "
            "Replace bbox with a verified glacial lake location."
        ),
        bbox=(85.30, 28.15, 85.40, 28.25),
        tags=["rasuwa", "langtang", "high-priority"],
    ),
]


# --- Data source settings -------------------------------------------------

SENTINEL_HUB_CONFIG = {
    # Set via environment variables, never commit real credentials.
    "client_id_env": "SENTINEL_HUB_CLIENT_ID",
    "client_secret_env": "SENTINEL_HUB_CLIENT_SECRET",
}

PLANET_CONFIG = {
    "api_key_env": "PLANET_API_KEY",
}
