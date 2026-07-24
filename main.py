import logging
import pandas as pd
import numpy as np
from pathlib import Path

from src.distance import compute_distance_matrix
from src.clustering import assign_agents_balanced
from src.optimizer import optimize_all_routes
from src.visualize import create_working_plot

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    data_dir = Path("data")
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    print("Loading dataset...")
    excel_file = data_dir / "TSP1.xlsx" if (data_dir / "TSP1.xlsx").exists() else data_dir / "TSP.xlsx"
    df = pd.read_excel(excel_file, sheet_name="Lat-Long")
    agents_df = pd.read_excel(excel_file, sheet_name="TSP agents")


    df = df.dropna(subset=['Latitude', 'Longitude']).reset_index(drop=True)
    df = df.drop_duplicates(subset=['Latitude', 'Longitude']).reset_index(drop=True)
    # Filter outlier coordinates (valid Lagos bounding box)
    df = df[(df['Latitude'] >= 6.0) & (df['Latitude'] <= 7.2) & (df['Longitude'] >= 2.8) & (df['Longitude'] <= 4.0)].reset_index(drop=True)

    
    print(f"Processed {len(df)} locations for {len(agents_df)} agents")

    coords = df[['Latitude', 'Longitude']].values
    dist_matrix = compute_distance_matrix(coords)

    df = assign_agents_balanced(df, agents_df, coords)
    df, metrics = optimize_all_routes(df, dist_matrix)

    df.to_excel(output_dir / "assigned_routes.xlsx", index=False)
    metrics.to_csv(output_dir / "route_summary_metrics.csv", index=False)

    create_working_plot(df, output_dir)
    print("[+] Done! Check outputs/ folder.")


if __name__ == "__main__":
    main()