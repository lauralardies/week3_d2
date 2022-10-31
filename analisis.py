import pandas as pd
import numpy as np 

data = pd.read_csv('vehicles_messy.csv')
print(data.head())
print(data.shape) # 5 rows x 83 columns