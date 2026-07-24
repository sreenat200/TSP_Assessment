import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from typing import List

def assign_agents_balanced(df: pd.DataFrame, agents_df: pd.DataFrame, coords: np.ndarray) -> pd.DataFrame:
    """Balanced spatial assignment using KMeans."""
    n_agents = len(agents_df)
    kmeans = KMeans(n_clusters=n_agents, random_state=42, n_init=10)
    labels = kmeans.fit_predict(coords)
    
    df = df.copy()
    df['Cluster'] = labels
    # map to agent names
    agent_names = agents_df['Agent Name'].tolist()
    df['Assigned_Agent'] = df['Cluster'].map(lambda x: agent_names[x % len(agent_names)])
    return df

cluster_locations = assign_agents_balanced