import numpy as np
from typing import Tuple

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Haversine formula for great-circle distance in km."""
    R = 6371.0  # earth radius
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return R * c

def haversine_distance_matrix(coords: np.ndarray) -> np.ndarray:
    """Vectorized pairwise distance matrix."""
    n = len(coords)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            dist = haversine_distance(*coords[i], *coords[j])
            matrix[i, j] = matrix[j, i] = dist
    return matrix