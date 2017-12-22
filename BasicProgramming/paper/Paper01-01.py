'''
<단순 변수 사용>
    1. 순차형
    1-1. 원의 둘레와 원의 넓이 계산
    1626035 이주호
'''

#반지름 입력
radius = int(input("원의 반지름 입력(정수) >> "))

#파이값 입력
PI = 3.14

#원의 둘레 계산
circumference = 2 * radius * PI

#원의 넓이 계산
area = (radius) * (radius) * PI

#결과 출력
print("원의 둘레: %.2f" % circumference)
print("원의 넓이: %.2f" % area)

