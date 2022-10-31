import pandas as pd
import numpy as np 

data = pd.read_csv('vehicles_messy.csv')
print(data.head())
print(data.shape) # 5 rows x 83 columns

# Vamos a ver el nombre de las columnas de nuestro dataframe, sus tipos de datos y los valores None
print(data.info())

# Creamos un df que cuenta los datos nulos de cada columna
nan_cols = data.isna().sum()
print(nan_cols[nan_cols > 0]) # Filtramos aquellas columnas que tengan algún valor nulo