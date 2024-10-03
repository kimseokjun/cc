import turtle
t= turtle.Turtle()

def n_polygon(n, length, position):
    for j in range(8):
        t.penup()
        t.goto(position,0)
        t.pendown()
        position += 100
        for i in range(n):
            t.forward(length)
            t.left(360//n)
        n+=1
            

position = int(input("시작 삼각형의 x좌표를 입력하세요."))
n_polygon(3,30,position)
