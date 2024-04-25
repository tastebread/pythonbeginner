#로또 추첨 번호

import random

#함수 선언 부분
def getNumber():
    return random.randint(1,46)

#전역 변수
lotto = []
num = 0

while True:
    num = getNumber()

    if lotto.count(num) == 0:
        lotto.append(num)

    if len(lotto) >=6:
        break

print("추첨된 로또 번호 == >  ", end='')
lotto.sort()
for i in range(0,6):
    print("%d " % lotto[i], end='')