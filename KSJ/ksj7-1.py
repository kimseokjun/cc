print("7-1. 20203035 김석준\n")

Fruits = []

while True:
    name = input("좋아하는 과일의 이름을 입력하시오 : ")
    if(name == '없음'):
        break
    else:
        Fruits.append(name)

Fruits.sort()
print("오름 차순 정렬 : \n", Fruits)
Fruits.sort(reverse=True)
print("내림 차순 정렬 : \n", Fruits)
