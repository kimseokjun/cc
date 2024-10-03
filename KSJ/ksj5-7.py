import random

while True:
    x = random.randint(1,100)
    y = random.randint(1,100)
    print("{} + {} =".format(x,y), end = " ")
    answer = int(input())
    if answer == x + y:
        print("잘했어요!!")
    else:
        print("정답은 {} 입니다, 다음번에는 잘할 수 있죠?".format(x+y))
    
