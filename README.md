# Route Optimization using Traveling Salesman Problem (TSP)

This project solves a route optimization problem by assigning retail shops to multiple sales agents and finding an efficient visiting order for each agent. The solution uses clustering to divide locations into balanced territories and then applies TSP optimization to reduce the travel distance for every agent.

---

## Project Overview

The dataset contains retail shop locations (latitude and longitude) and a list of 41 sales agents.

The project follows these steps:

* Load and clean the dataset
* Remove invalid and duplicate coordinates
* Group nearby shops using K-Means clustering
* Assign one agent to each cluster
* Optimize the route for every agent using Nearest Neighbor and 2-Opt
* Export the final assignments and summary reports
* Generate a map showing all optimized routes

---

## Project Structure

```text
TSP_Assessment/
│
├── data/
│   └── TSP.xlsx
│
├── outputs/
│   ├── assigned_routes.xlsx
│   ├── route_summary_metrics.csv
│   └── routes_map.png
│
├── src/
│   ├── __init__.py
│   ├── distance.py
│   ├── clustering.py
│   ├── optimizer.py
│   └── visualize.py
│
├── approach_explanation.txt
├── solution_notebook.ipynb
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/sreenat200/TSP_Assessment.git
cd TSP_Assessment
```

Create a virtual environment.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

---

## Run the Project

Run the complete pipeline with:

```bash
python main.py
```

Or open the notebook:

```bash
jupyter notebook solution_notebook.ipynb
```

---

## Approach

### 1. Data Cleaning

The dataset is loaded using pandas.

Before processing, the data is checked for:

* Missing values
* Duplicate records
* Invalid latitude and longitude values

A geographic boundary is also used to remove locations that are outside the Lagos area.

---

### 2. Distance Calculation

Distances are calculated using the Haversine formula.

This provides more accurate results than straight-line distance because it considers the Earth's curvature.

To improve performance, the calculations are vectorized using NumPy.

---

### 3. Customer Assignment

K-Means clustering is used to divide the locations into 41 clusters.

Each cluster is assigned to one sales agent.

Grouping nearby shops together helps reduce unnecessary travel.

---

### 4. Route Optimization

After clustering, the visiting order inside each cluster is optimized.

The process uses:

* Nearest Neighbor to create an initial route.
* 2-Opt to improve the route by removing unnecessary crossings.

This helps reduce the total travel distance.

---

### 5. Visualization

The project generates a route map where:

* Each agent has a different color.
* Customer locations are displayed.
* Routes follow Earth-curved paths based on GPS coordinates.

---

## Output Files

After running the project, the following files are created inside the **outputs** folder.

### assigned_routes.xlsx

Contains:

* Original shop information
* Assigned agent
* Cluster ID
* Route order

### route_summary_metrics.csv

Contains:

* Agent name
* Number of stops
* Total distance
* Average distance

### routes_map.png

A visualization showing all optimized routes with different colors for each agent.

---

## Libraries Used

* pandas
* numpy
* scikit-learn
* matplotlib
* openpyxl

---

## Future Improvements

Some possible improvements are:

* Better balanced clustering using capacity constraints
* More advanced optimization algorithms such as Genetic Algorithms or OR-Tools
* Interactive route visualization using Folium
* Parallel route optimization for larger datasets

---

## Repository

GitHub: https://github.com/sreenat200/TSP_Assessment

This project was built as part of a route optimization assignment using clustering and Traveling Salesman Problem (TSP) techniques.
