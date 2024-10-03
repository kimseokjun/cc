print("8-2.    20203035 김석준")

items = {"콜라" : 4, "환타" : 10, "제로콜라" : 3}

while True:
    num = int(input("메뉴를 선택하시오 1) 재고조회 2) 입고 3) 출고 4) 종료 : "))
    if num == 1:
        name = input("[재고조회] 물건의 이름을 입력하시오 : ")
        print("{}의 재고 : {}".format(name,items[name]))
    elif num == 2:
        name ,plus = input("[입고] 물건의 이름과 수량을  입력하시오 : ").split()
        items[name] += int(plus)
    elif num == 3:
        name ,minus = input("[출고] 물건의 이름과 수량  입력하시오 : ").split()
        items[name] -= int(minus)
    elif num == 4:
        print(" 프로그램을 종료합니다.")
        break;
