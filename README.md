# REFUGEES & ASYLUM SEEKERS 
This project tries to analyze refugees and asylum seekers in Indonesia, and then also analyze Indonesians who are refugees and asylum seekers to find other countries to live in. This analysis aims to make new innovation graphs into visuals for open source using python. Temporary Data source collection from [UNHCR in Data World in Noah Ripper's account on Refugee Host Countries](https://data.world/nrippner/refugee-host-nations). Hopefully this project will be a guide for open source and transpiration.

## Create Dataframe from Data Base 
```python

import csv 
import pandas as pd
datarefugeesidn1115 = pd.read_csv("/Users/mymac/Desktop/Data Github/datarefugeesidn.csv", delimiter=';', header = None) # adjust columns and rows
datarefugeesidn1115.columns = ['Year', 'Country', 'Origin', 'Refugees', 'AsylumSeekers', 'Total'] # create columns
datarefugeesidn1115 = datarefugeesidn1115.iloc[1:] # delete more columns
print(datarefugeesidn1115) #view data

```
