import turtle

swidth, sheight = 500, 500
turtle.title('무지개색 원 그리기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.goto(0, -sheight / 2)
turtle.pendown()
turtle.speed(200)

for rad in range(1,250):
    if rad % 7 == 1:
        turtle.pencolor('red')
    elif rad % 7 == 2 :
        turtle.pencolor('orange')
    elif rad % 7 == 3:
        turtle.pencolor('yellow')
    elif rad % 7 == 4:
        turtle.pencolor('green')
    elif rad % 7 == 5:
        turtle.pencolor('blue')
    elif rad % 7 == 6:
        turtle.pencolor('navyblue')
    else:
        turtle.pencolor('purple')

    turtle.circle(rad)
turtle.done()