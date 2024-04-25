#동전 교환기 만들기

#변수 선언
money,c500,c100,c50,c10 = 0,0,0,0,0

#메인 코드 부분
money = int(input("교환할 돈은 얼마? : "))

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print("\n 500원 짜리 == > {}개".format(c500))
print(" 100원 짜리 == > {}개".format(c100))
print(" 50원 짜리 == > {}개".format(c50))
print(" 10원 짜리 == > {}개".format(c10))
print(" 바꾸지 못한 잔돈 ==> {}원\n ".format(money))

