from tkinter import *

windows = Tk()
##이부분에서 화면을 구성하는 코드
"""
windows.title("윈도우창 연습")
windows.geometry("400x100")
windows.resizable(width = FALSE, height = FALSE)
"""
"""
label1 = Label(windows, text="야 이거 맞냐?")
label2 = Label(windows, text="공부중",font = ('AppleGothic',30), fg='blue')
label3 = Label(windows, text="공부 중입니다.",bg="magenta",width=20,height=5,anchor = SE)
# bg -> background 약어 배경색지정 , anchor 위젯이 어느 위치에 자리 잡을지 결정.
label1.pack()
label2.pack()
label3.pack()

"""
photo = PhotoImage(file = "/Users/tastebread/Desktop/pythonbeginner/ch10/pic1.gif")
label1 = Label(windows, image=photo)

label1.pack()
windows.mainloop()
