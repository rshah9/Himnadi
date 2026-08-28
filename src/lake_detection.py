"""
Extract water-body extent (glacial lake area) from a satellite image.

Starting approach: NDWI (Normalized Difference Water Index) thresholding
on Sentinel-2 imagery. It's simple and well-established as a first pass,
though it struggles with shadow and thin cloud, and doesn't work on SAR
imagery directly (SAR needs a different approach — backscatter thresholding).

NDWI = (Green - NIR) / (Green + NIR)
Water typically has NDWI > 0; land/vegetation typically < 0.
"""

from __future__ import annotations

import numpy as np


def compute_ndwi(green_band: np.ndarray, nir_band: np.ndarray) -> np.ndarray:
    """Compute NDWI from green and near-infrared bands (as float arrays)."""
    green = green_band.astype("float32")
    nir = nir_band.astype("float32")
    denom = green + nir
    # avoid divide-by-zero
    denom[denom == 0] = 1e-6
    return (green - nir) / denom


def extract_water_mask(ndwi: np.ndarray, threshold: float = 0.0) -> np.ndarray:
    """Boolean mask of pixels classified as water."""
    return ndwi > threshold


def water_area_m2(water_mask: np.ndarray, pixel_size_m: float) -> float:
    """
    Convert a water mask to an area in square meters, given the pixel
    resolution (e.g. 10.0 for Sentinel-2 10m bands).
    """
    pixel_area = pixel_size_m**2
    return float(water_mask.sum()) * pixel_area


# TODO: add a SAR-based water extraction path (backscatter thresholding)
# for Sentinel-1, since it works through cloud cover during monsoon season
# when optical imagery is often unusable.
