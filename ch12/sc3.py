class Car:
    color = ""
    speed = 0

    def __init__(self,value1,value2):
        self.color = value1
        self.speed = value2

    def upSpeed(self,value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150
    def downSpeed(self,value):
        self.speed -= value

    def printMessage():
        print("시험 출력이다")

myCar1 = Car("빨강",30)
myCar2 = Car("파랑",60)

print("자동차1의 색상은 {}이며 현재 속도는 {}km 입니다".format(myCar1.color,myCar1.speed))
print("자동차2의 색상은 {}이며 현재 속도는 {}km 입니다".format(myCar2.color,myCar2.speed))