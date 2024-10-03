print('\n12-9.20203035 김석준  \n')
import pandas as pd

weather = pd.read_csv('c:/temp/data/weather.csv', index_col = 0, encoding='CP949')
missing_data = weather [ weather['평균풍속'].isna() ] 
print(missing_data)

weather = pd.read_csv('c:/temp/data/weather.csv', index_col = 0, encoding='CP949')
weather.fillna(0, inplace = True) 
print()
print(weather.loc['2012-02-11'])

weather = pd.read_csv('c:/temp/data/weather.csv', index_col = 0, encoding='CP949')
weather.fillna( weather['평균풍속'].mean(), inplace = True)
print()
print(weather.loc['2012-02-11'])
