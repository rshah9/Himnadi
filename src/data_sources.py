"""
Clients for fetching satellite imagery for a monitored site.

This is a skeleton. Fill in real API calls once you've picked which
provider(s) to start with. Sentinel Hub is recommended first: it's free
for research use, has a Python SDK (sentinelhub-py), and Sentinel-1's
SAR imagery penetrates cloud cover, which matters a lot for the
monsoon-affected Himalaya.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from config import MonitoredSite


@dataclass
class ImageryResult:
    site_id: str
    acquired_date: date
    source: str  # e.g. "sentinel-2", "sentinel-1", "planet"
    image_path: str  # local path to downloaded raster
    cloud_cover_pct: float | None = None


def fetch_sentinel2_imagery(
    site: MonitoredSite, start: date, end: date
) -> list[ImageryResult]:
    """
    Fetch Sentinel-2 optical imagery for a site's bounding box over a date
    range.

    TODO:
      - Install `sentinelhub` (pip install sentinelhub) and configure
        credentials via SENTINEL_HUB_CLIENT_ID / SECRET env vars.
      - Use a low-cloud-cover filter; optical imagery is useless if the
        lake is obscured, which is common during monsoon season.
      - Cache downloaded imagery under data/ to avoid re-fetching.
    """
    raise NotImplementedError(
        "Wire this up to the Sentinel Hub API. See "
        "https://sentinelhub-py.readthedocs.io/"
    )


def fetch_sentinel1_imagery(
    site: MonitoredSite, start: date, end: date
) -> list[ImageryResult]:
    """
    Fetch Sentinel-1 SAR imagery — works through cloud cover, which makes
    it more reliable than optical during monsoon season.

    TODO: same as fetch_sentinel2_imagery, but request SAR products
    (GRD) instead of optical.
    """
    raise NotImplementedError("Wire this up to the Sentinel Hub API (SAR/GRD).")


def fetch_planet_imagery(
    site: MonitoredSite, start: date, end: date
) -> list[ImageryResult]:
    """
    Fetch Planet Labs imagery, if you have research/disaster-response
    access. Higher resolution than Sentinel, but commercial.
    """
    raise NotImplementedError("Wire this up to the Planet API.")
