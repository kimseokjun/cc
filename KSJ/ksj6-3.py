import turtle
t= turtle.Turtle()
t.speed(0)

def drawBar(height):
    t.begin_fill()
    if(height<100):
        t.fillcolor("blue")
    elif(height<300):
        t.fillcolor("yellow")
    else:
        t.fillcolor("red")
    t.left(90)
    t.forward(height)
    t.write(str(height), font = ('Times New Roman',16,'bold'))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

for height in [120,56,309,220,156,23,98]:
    drawBar(height)
t.penup()
t.goto(-100,200)
t.pendown()
t.write(str("김석준 20203035"), font = ('Times New Roman',16,'bold'))
