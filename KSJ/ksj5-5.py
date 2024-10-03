import turtle

t= turtle.Turtle()
t.speed(0)
t.width(1)
go = 0
length = 10
while True :
    angle=(int(input("각도를 입력하세요 : ")))
    if(angle < 0):
        break
    for length in range(100):
        t.forward(length)
        t.right(angle)
    go += 150
    t.penup()
    t.goto(go,0)
    t.pendown()
    length =0
