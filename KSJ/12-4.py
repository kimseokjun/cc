print('\n12-4. 20102000 Hong홍길동 \n')
import pandas as pd
df = pd.read_csv('c:/temp/data/countries.csv')
print(df)
print('\n', df.tail())
print('\n', df[3:6])
