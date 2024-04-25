import turtle
import random

##전역 변수 지정
swidth,sheight,pSize,exitcount = 300,300,3,0
r,g,b,angle,dist,curX,curY = [0] * 7

turtle.title("거북이 마음대로 가보게 해보자잇")
turtle.shape("turtle")
turtle.pensize(pSize)
turtle.setup(width = swidth + 30, height = sheight + 30)
turtle.screensize(swidth,sheight)

while True:
    r = random.random()
    g = random.random()
    b = random.random()

    angle = random.randrange(0,360)
    dist = random.randrange(1,100)
    turtle.left(angle)
    turtle.right(dist)
    curX = turtle.xcor()
    curY = turtle.ycor()


    if (-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2):
        pass
    else:
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()

        exitcount += 1
        if exitcount >= 5:
            break

    turtle.done()