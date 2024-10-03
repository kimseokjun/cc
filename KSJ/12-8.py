print('\n12-8. 20203035 김석준  \n')
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
weather = pd.read_csv('c:/temp/data/weather.csv', encoding='CP949')
weather['month'] = pd.DatetimeIndex(weather['일시']).month
# old version에서 가능 # means = weather.groupby('month').mean()
means = weather[['평균기온', 'month']].groupby('month').mean()
means['평균기온'].plot(kind='bar')
plt.title('12-8. 20203035 김석준')
plt.show()
