import turtle

t= turtle.Turtle()

t.shape("turtle")

 

t.penup()

t.goto(100,100)

t.write("두수 모두 양수입니다.")

t.goto(-100,100)

t.write("첫번째 수만 음수입니다.")

t.goto(-100,-100)

t.write("두수 모두 음수입니다.")

t.goto(100,-100)

t.write("두 번째 수만 음수")

 

t.goto(0,0)

t.pendown()

 

s1 = turtle.textinput("","첫번째 숫자를 입력하시오:")

s2 = turtle.textinput("","두번째 숫자를 입력하시오:")

x = int(s1)

y = int(s2)

 

if(x>0) :

    if(y>0) :

        t.goto(100,100)

    elif(y<0) :

        t.goto(100,-100)

if(x<0) :

    if(y>0):

        t.goto(-100,100)

    elif(y<0):

        t.goto(-100,-100)
