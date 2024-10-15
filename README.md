# REFUGEES & ASYLUM SEEKERS 
This project tries to analyze refugees and asylum seekers in Indonesia, and then also analyze Indonesians who are refugees and asylum seekers to find other countries to live in. This analysis aims to make new innovation graphs into visuals for open source using python. Temporary Data source collection from [UNHCR in Data World in Noah Ripper's account on Refugee Host Countries](https://data.world/nrippner/refugee-host-nations). Hopefully this project will be a guide for open source and transpiration.

## Refugees & Aslyem Seekers 2011-2015 in Indonesia
### Create Dataframe from Data Base 
```python

import csv 
import pandas as pd
datarefugeesidn1115 = pd.read_csv("/Users/mymac/Desktop/Data Github/datarefugeesidn.csv", delimiter=';', header = None) # adjust columns and rows
datarefugeesidn1115.columns = ['Year', 'Country', 'Origin', 'Refugees', 'AsylumSeekers', 'Total'] # create columns
datarefugeesidn1115 = datarefugeesidn1115.iloc[1:] # delete more columns
print(datarefugeesidn1115) #view data

```
### Refugees & Aslyem Seekers
```python

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

```
![Data Refugees & Aslyum Seekers](datavisual/refugees&asylumseekersidn20112015.png)
