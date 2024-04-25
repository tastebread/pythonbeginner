import turtle
import random

pSize,tSize = 10, 0
r,g,b = 0.0,0.0,0.0

def screenClick(x,y):
    global r,g,b
    turtle.pencolor((r,g,b))
    #turtle.pendown()
    turtle.stamp()
    #turtle.goto(x,y)

def screenRightClick(x,y):
    turtle.penup()
    turtle.goto(x,y)

def screenMidClick(x,y):
    global r,g,b
    tSize = random.randrange(1,10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenClick,1)
turtle.onscreenclick(screenRightClick,2)
turtle.onscreenclick(screenMidClick,3)

turtle.done()