print('\n12-2. 20203035 김석준  \n')
import csv     
f = open('C:/temp/data/weather.csv')  
data = csv.reader(f)             
header = next(data)

monthly_wind = [0 for x in range(12)]
days_counted = [ 0 for x in range(12)]


for row in data:
    month = int(row[0][5:7])
    if row[3] != '':
        wind = float(row[3])
        month;y_wind[month-1] += wind
        days_counted[month-1] += 1

for i in range(12):
    monthly_wind[i] /= days_counted[i]

plt.plot(monthly_wind,'blue')

f.close()
        
