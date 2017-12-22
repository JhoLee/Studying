## 변수 초기화
money = 0

## 데이터 입력
money = int(input("교환할 금액 입력 >> "))

## 교환
_10000won = money / 10000
money %= 10000
_1000won = money / 1000
money %= 1000
_100won = money / 100
money %= 100
_10won = money / 10
money %= 10

## 출력
print("%d만 %d천 %d백 %d십 %d원" % (_10000won, _1000won, _100won, _10won, money))
