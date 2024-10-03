print("7-4. 20203035 김석준\n")

city_info = []

while True:
    city_pop = input("도시명, 인구를 입력하세요 : ")
    if(city_pop == "0 0"):
        break
    x, y = city_pop.split( )
    city_info.append((x, int(y)))

print(city_info)

max_pop = 0
min_pop = 999999999999999
total_pop = 0

max_city = None
min_city = None
for city in city_info:
    total_pop += city[1]
    if city[1] > max_pop:
        max_pop = city[1]
        max_city = city
    if city[1] < min_pop:
        min_pop = city[1]
        min_city = city   

print("최대인구: {}, 인구: {} 만명".format(max_city[0],max_city[1]))
print("최소인구: {}, 인구: {} 만명".format(min_city[0],min_city[1]))
print("리스트 도시 평균 인구: {} 만명".format(total_pop / len(city_info)))
