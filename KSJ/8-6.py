print("8-6.    20203035 김석준")


fruits_price = {"사과" : 0, "배" : 0, "수박" : 0, "귤" : 0, "포도" : 0}

fruits_price["사과"], fruits_price["배"], fruits_price["수박"], fruits_price["귤"] ,fruits_price["포도"] = input("사과, 배, 수박, 귤 , 포도, 가격을 공백으로 구분하여 입력 : ").split()
print("----------------------오늘의 과일 가격--------------------------\n")
for key in fruits_price.keys():
    print(key, ":", fruits_price[key],"원")
while True:
    name = input(".구매를 원하는 과일의 이름을 입력하시오 : ")
    print("오늘의 {} 가격은 {}원 입니다.".format(name,fruits_price[name]))
