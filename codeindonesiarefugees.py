# Refugees & Asylum Seekers in Indonesia (2011-2015)
import csv 
import pandas as pd
datarefugeesidn1115 = pd.read_csv("/Users/mymac/Desktop/Data Github/datarefugeesidn.csv", delimiter=';', header = None) # adjust columns and rows
datarefugeesidn1115.columns = ['Year', 'Country', 'Origin', 'Refugees', 'AsylumSeekers', 'Total'] # create columns
datarefugeesidn1115 = datarefugeesidn1115.iloc[1:] # delete more columns
print(datarefugeesidn1115) #view data

# Create Graph Analysis

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style # import theme
print(plt.style.available) # list theme 

font1 = {'family':'serif','color':'black','size':20} #for title graph visual
plt.figure(figsize=(10,6))
sns.scatterplot(x = "Refugees", y ="AsylumSeekers", data = datarefugeesidn1115,
hue= "Year", palette="Set1")
plt.xlabel("Refugees")
plt.ylabel("Asylum Seekers")
plt.title("Refugees & Asylum Seekers in Indonesia (2011-2015)", fontdict = font1)
max_refugees_idx = datarefugeesidn1115["Refugees"].idxmax()
max_asylum_seekers_idx = datarefugeesidn1115["AsylumSeekers"].idxmax()
dominat_x = datarefugeesidn1115["Refugees"].iloc[max_refugees_idx]
dominant_y = datarefugeesidn1115["AsylumSeekers"].iloc[max_asylum_seekers_idx]
circle = plt.Circle((dominat_x, dominant_y), 150, color='black', fill=False, linewidth=1)
plt.gca().add_artist(circle)
plt.text(x=1681, y=3782, s="Afghanistan", fontsize=12, color='black', fontweight='bold')
plt.text(x=208, y =1649, s="Iran", fontsize=12, color='black',fontweight='bold')
plt.text(x=781, y=711, s="Myanmar", fontsize=12, color='black', fontweight='bold')
plt.text(x=448, y=724, s="Somalia", fontsize=12, color='black', fontweight='bold')
plt.text(x=217, y=1489, s="Iraq", fontsize=12, color='black', fontweight='bold')
plt.tight_layout()
plt.style.use('seaborn-v0_8-white') #theme
plt.show()

#==============================================================================

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# file data from nautural earth # https://www.naturalearthdata.com/

world = gpd.read_file("/Users/mymac/Desktop/Data Github/ne_110m_admin_0_countries.shp")
world = gpd.read_file("/Users/mymac/Desktop/Data Github/ne_110m_admin_0_countries.dbf")
world = gpd.read_file("/Users/mymac/Desktop/Data Github/ne_110m_admin_0_countries.shx")


indonesianrefugeesseekers = {
    'Country': ["Australia", "Canada", "Germany", "France", "United Kingdom", "Greece",
                "Japan", "South Korea", "Malaysia", "Netherlands", "Papua New Guinea", 
                "Sweden", "United States of America"],
    'Indonesian': [494, 321, 27, 6, 24, 12, 854, 7, 819, 22, 9368, 20, 4162]
}

# Dictionary country coordinate  (longitude, latitude)
coords = {
    "Australia": (133.7751, -25.2744),
    "Canada": (-106.3468, 56.1304),
    "Germany": (10.4515, 51.1657),
    "France": (2.2137, 46.6034),
    "United Kingdom": (-3.4360, 55.3781),
    "Greece": (21.8243, 39.0742),
    "Japan": (138.2529, 36.2048),
    "South Korea": (127.7669, 35.9078),
    "Malaysia": (101.9758, 4.2105),
    "Netherlands": (5.2913, 52.1326),
    "Papua New Guinea": (147.1803, -6.3149),
    "Sweden": (18.6435, 60.1282),
    "United States of America": (-95.7129, 37.0902)
}

# convert to DataFrame
indonesianrefugeesseekers2015 = pd.DataFrame(indonesianrefugeesseekers)

print(indonesianrefugeesseekers2015)

#combine dataframe with world (data Shapefile)
world = world.merge(indonesianrefugeesseekers2015, how="left", left_on="SOVEREIGNT", right_on="Country")

font1 = {'family':'serif','color':'black','size':15} #for title graph visual

# plot maps world
fig, ax = plt.subplots(1, 1, figsize=(30, 12))

# plot chorpleth
world.boundary.plot(ax=ax) 
world.plot(column='Indonesian', ax=ax, legend=True,
cmap='OrRd',
missing_kwds={'color':'lightgrey'},
legend_kwds={'label':"Indonesian",
'orientation': "horizontal"})

world['centroid'] = world.geometry.centroid
plt.title("Indonesian Refugees & Asylum Seekers 2014 to 2015", fontdict=font1)
plt.show()


# Indonesian Refugees & Asylum Seekers (2011 - 2015)
import pandas as pd
import plotly.graph_objects as go


# Data for Refugees
indonesianrefugee = pd.DataFrame({
    'Year': [2011, 2012, 2013, 2014, 2015],
    'Refugees': [16079, 15523, 14786, 14393, 13942]
})

# Data for Seekers
indonesianseekers = pd.DataFrame({
    'Year': [2011, 2012, 2013, 2014, 2015],
    'Seekers': [429, 506, 1968, 1892, 2194]
})

# create Figure
fig = go.Figure()

# add trace for Refugees
fig.add_trace(go.Scatter(x=indonesianrefugee['Year'],
                         y=indonesianrefugee['Refugees'],
                         mode='lines+markers',
                         name="Indonesian Refugees",
                         marker=dict(color='red'),
                         line=dict(color='red')))

# add trave for Seekers
fig.add_trace(go.Scatter(x=indonesianseekers['Year'],
                         y=indonesianseekers['Seekers'],
                         mode='lines+markers',
                         name="Indonesian Seekers",
                         marker=dict(color='blue'),
                         line=dict(color='blue')))

# Update layout for title and element or others
fig.update_layout(title="Indonesian Refugees & Asylum Seekers 2011 - 2015",
                  xaxis_title="Years",
                  yaxis_title="Indonesian",
                  plot_bgcolor='rgb(17,17,17)',
                  paper_bgcolor='rgb(17,17,17)',
                  font=dict(color="white"),
                  xaxis=dict(showgrid=False),
                  yaxis=dict(showgrid=False),
                  showlegend=True)
                  
fig.update_xaxes(tickvals=[2011,2012,2013,2014,2015])

# show plot
fig.show()

