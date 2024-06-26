import turtle
import random
from tkinter.simpledialog import *

#전역 변수 부분
inStr = ''
swidth, sheight = 300,300
tX,tY,txtSize = [0] * 3

#메인코드
turtle.title('거북이 글자쓰기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height= sheight + 50)
turtle.screensize(swidth,sheight)
turtle.penup()

inStr = askstring('문자열 입력','거북이 쓸 문자열 입력')
print(type(inStr))

for ch in inStr:
    tX = random.randrange(-swidth / 2, swidth / 2)
    tY = random.randrange(-sheight / 2, sheight / 2)
    r = random.random(); g = random.random(); b = random.random()
    txtSize = random.randrange(10,50)

    turtle.goto(tX,tY)

    turtle.pencolor((r,g,b))
    turtle.write(ch, font=('AppleGothic',txtSize,'bold'))

turtle.done()