## 변수 초기화
radius = 0
circumference = 0
area = 0
PI = 3.14

## 입력
radius = float(input("반지름 >> "))

## 계산
circumference = 2 * PI * radius
area = PI * PI * radius

## 출력
print("원의 반지름 : %.2f" % radius)
print("원의 둘레 : %.2f" % circumference)
print("원의 넓이 : %.2f" % area)
