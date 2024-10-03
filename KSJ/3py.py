import turtle
t = turtle.Turtle()
t.shape("turtle")
while True :
    n= int(input("몇각형을 그리시겠어요?"))
    if(360%n != 0) :
        print("회전각도가 정수가 아닙니다.\n")
        continue
    for i in range(n) :
        t.forward(100)
        t.left(360//n)
turtle.done()
