print('\n12-5. 20203035 김석준  \n')
import pandas as pd
import matplotlib.pyplot as plt

countries_df = pd.read_csv('c:/temp/data/countries.csv', index_col = 0)

countries_df[5:10]['population'].plot(kind = 'bar', color=('b', 'darkorange', 'g','r','m'))
#countries_df[5:10]['population'].plot(kind= 'pie')
plt.show()
