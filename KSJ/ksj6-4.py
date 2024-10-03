import turtle

t= turtle.Turtle()
t.shape("turtle")
t.speed(0)

def f(x):
    return x**2

t.goto(-300,0)
t.goto(0,0)
t.goto(300,0)
t.goto(0,0)
t.goto(0,300)
t.goto(0,0)
t.penup()
t.goto(-150,int(0.01*f(-150)))
t.pendown()

for x in range(-150,150):
    t.goto(x, int(0.01*f(x)))
