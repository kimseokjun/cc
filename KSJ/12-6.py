print('\n12-6. 20203035 김석준  \n')
import pandas as pd
import matplotlib.pyplot as plt 
countries_df = pd.read_csv('c:/temp/data/countries.csv', index_col = 0)
countries_df['denstiy'] = countries_df['population']/countries_df['area']
print(countries_df[0:7])
