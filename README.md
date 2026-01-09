# NG Figure Reproduction

This repository houses Python scripts and supporting data used to regenerate the published Figure 1 to Figure 3. Each script reads the data stored under `data/` and writes the rendered artwork to `figure/`.

## Citation

If you use this code or data, please cite:

> Zhang, Y., Blöschl, G., Wei, H. et al. Overestimation of past and future increases in global river flow by Earth system models. *Nat. Geosci.* (2026). https://doi.org/10.1038/s41561-025-01897-9

## Repository Layout
- `code/fig1.py` - builds the multi-panel Figure 1, including the global map assembled from basin shapefiles.
- `code/fig3.py` - builds the bar charts for Figure 3 using the processed tabular data.
- `data/Data for main figures.csv` - source table that feeds Figure 3.
- `data/shp/` - collection of 50 basin shapefiles consumed by Figure 1 (already unpacked from `50LargeRiverBasins.zip`).
- `figure/` - target folder for rendered PNG outputs.

## Prerequisites
- Python 3.9 or later.
- A working installation of the following Python packages:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `brokenaxes`
  - `cartopy`
  - `geopandas`

> **Cartopy/GeoPandas note** - for spatial dependencies (GEOS, PROJ, shapely) the `conda-forge` channel is the most reliable source. When using `pip`, make sure the system libraries that Cartopy needs are present.

### Suggested Conda Setup
```bash
conda create -n ng-figure python=3.10
conda activate ng-figure
conda install -c conda-forge numpy pandas matplotlib cartopy geopandas brokenaxes proj-data
```
If you prefer `pip`, install the wheel packages after ensuring the geospatial dependencies are available:
```bash
pip install numpy pandas matplotlib brokenaxes cartopy geopandas
```

## Data Preparation
The repository already contains the required inputs. If you start from a fresh clone and only see `50LargeRiverBasins.zip`, unzip it so that every basin directory lives under `data/shp/` as expected by `fig1.py`. No further preprocessing is required for the CSV file used by Figure 3.

## How to run & reproduce the figures
1. Activate the environment that has the dependencies installed.
2. Run the script from the project root (or from inside `code/`):
   ```bash
   python code/fig1.py
   python code/fig3.py
   ```
3. The script scans `data/shp/` recursively for `.shp` files and draws them on a Robinson-projection map alongside several analytical panels.
4. The rendered artwork is saved to `figure/fig1.png`. The script also opens a preview window if a graphical backend is available.
5. The rendered artwork is saved to `figure/fig3.png`. The script also opens a preview window if a graphical backend is available.
