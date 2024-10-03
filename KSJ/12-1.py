print("12-1. 20203035 김석준")
import csv
f = open('c:/Temp/data/weather.csv')
i=0
data = csv.reader(f)
for row in data:
    print(row)
    i= i+1
    if(i==11):
        break
f.close()
