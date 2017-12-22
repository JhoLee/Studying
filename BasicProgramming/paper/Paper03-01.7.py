'''
<단순 변수 사용>
    3. 반복형
    3-1. 수열의 수 도출과 누적 값
        7) 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 33 + 54
            - 피보나치 수열의 1항부터 10항까지의 합
    1626035 이주호
'''

#변수 초기화
sum = 0
i = 0
a = 0
b = 1
c = 0


##계산
print("n항 (n-1)항 누적합")
for i in range(1, 10+1):
    c = b
    b = a
    a = b + c
    sum = sum + a
    print("%3d %6d %6d " % (a, b, sum, ))
##계산 종료

#결과 출력
print("1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 33 + 54 = %d" % (sum))
