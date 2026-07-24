import numpy as np
import pandas as pd
from typing import Tuple, List
from itertools import permutations  # fallback for small routes

def nearest_neighbor_route(dist_matrix: np.ndarray, start_idx: int = 0) -> List[int]:
    """Simple Nearest Neighbor heuristic."""
    n = len(dist_matrix)
    visited = [False] * n
    route = [start_idx]
    visited[start_idx] = True
    current = start_idx

    for _ in range(n - 1):
        nearest = np.argmin([dist_matrix[current, j] if not visited[j] else np.inf for j in range(n)])
        route.append(nearest)
        visited[nearest] = True
        current = nearest
    return route

def two_opt(route: List[int], dist_matrix: np.ndarray) -> List[int]:
    """2-Opt improvement."""
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                if dist_matrix[route[i-1], route[j]] + dist_matrix[route[i], route[j+1]] < \
                   dist_matrix[route[i-1], route[i]] + dist_matrix[route[j], route[j+1]]:
                    route[i:j+1] = route[i:j+1][::-1]
                    improved = True
    return route

def optimize_route(indices: List[int], dist_matrix: np.ndarray) -> Tuple[List[int], float]:
    if len(indices) <= 1:
        return indices, 0.0
    route = nearest_neighbor_route(dist_matrix[np.ix_(indices, indices)], 0)
    route = [indices[i] for i in route]
    route = two_opt(route, dist_matrix)
    total_dist = sum(dist_matrix[route[i], route[i+1]] for i in range(len(route)-1))
    return route, total_dist

def optimize_all_routes(df: pd.DataFrame, dist_matrix: np.ndarray) -> Tuple[pd.DataFrame, pd.DataFrame]:
    results = []
    metrics = []
    
    for agent, group in df.groupby('Assigned_Agent'):
        indices = group.index.tolist()
        if not indices:
            continue
        route_order, total_dist = optimize_route(indices, dist_matrix)
        
        # build ordered rows
        ordered_group = group.loc[route_order].copy()
        ordered_group['Route_Order'] = range(1, len(ordered_group) + 1)
        results.append(ordered_group)
        
        metrics.append({
            'Agent': agent,
            'Stops': len(group),
            'Total_Distance_km': round(total_dist, 2),
            'Avg_Distance_per_Stop_km': round(total_dist / len(group), 2) if len(group) > 0 else 0
        })
    
    final_df = pd.concat(results).sort_values(['Assigned_Agent', 'Route_Order'])
    metrics_df = pd.DataFrame(metrics)
    return final_df, metrics_df

# for backwards compatibility
solve_tsp = optimize_all_routes