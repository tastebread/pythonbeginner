#윤년 계산 프로그램

num = int(input("연도를 입력하세요 : "))

if ((num % 4 == 0) and(num % 100 != 0)) or (num % 400 == 0):
    print("{}은 윤년입니다".format(num))
else:
    print("윤년이 아닙니다..")