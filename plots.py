import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# read in CSV generated in ArcGIS
data = pd.read_csv(r'data/Final_Points_Statistics_Exported.csv')

data_sorted = data.sort_values(by='MEAN_ELEVATION')

# define custom color map
colors = [(0.3, 0.6, 0.3), (0.8, 0.8, 0.4), (0.6, 0.4, 0.3)]
custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", colors, N=256)

scatter_plot = plt.scatter(
    x=data_sorted['LANDCOVER_T'], y=data_sorted['MEAN_ELEVATION'],
    c=data_sorted['MEAN_ELEVATION'],
    cmap=custom_cmap,
    s=100
)

# customise plot
colorbar = plt.colorbar(scatter_plot, orientation='vertical', pad=0.03)
colorbar.set_ticks([])
plt.xlabel("Landcover Type")
plt.ylabel("Elevation")
plt.xticks(rotation=70, fontsize=8)

# output plot
plt.show()
