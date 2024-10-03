print("7-2. 20203035 김석준\n")

population = ["Seoul", 9765, "Busan",3441, "Incheon",2954]

print("서울 인구 : ",population[1])
print("인천 인구 : ",population[-1])

cities = population[0::2]
print("도시 리스트: ",cities)
pop = population[1::2]
print("인구의 합 : " , sum(pop))
