import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

def plot_routes(df: pd.DataFrame, save_path: Path):
    """Earth-curved route visualization with distinct colors per agent."""
    plt.figure(figsize=(14, 10))
    colors = plt.cm.tab20(np.linspace(0, 1, df['Assigned_Agent'].nunique()))
    
    for idx, (agent, group) in enumerate(df.groupby('Assigned_Agent')):
        color = colors[idx % len(colors)]
        # Sort by route order
        sorted_group = group.sort_values('Route_Order')
        lats = sorted_group['Latitude']
        lons = sorted_group['Longitude']
        
        plt.plot(lons, lats, 'o-', color=color, alpha=0.7, linewidth=1.5, label=agent)
        plt.scatter(lons, lats, color=color, s=30, edgecolor='black', zorder=5)
    
    plt.title('TSP Routes by Agent - Lagos Area', fontsize=16)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()