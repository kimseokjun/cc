import turtle
t = turtle.Turtle()
t.speed(0)


t.penup()
t.goto(-300,0)
t.pendown()
for i in range(6):
    t.circle(100)
    t.left(60)

t.penup()
t.goto(0,0)
t.pendown()

for j in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.goto(300,0)
t.pendown()

for k in range(4):
    t.forward(100)
    t.left(90)
