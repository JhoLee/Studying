'''
<단순 변수 사용>
    3. 반복형
    3-1. 수열의 수 도출과 누적 값
        3) 1 - 2 + 3 - .. - 100
            1~100 까지의 수들 중, 홀수는 더하고 짝수는 뺀다.
            - Switch 형식
    1626035 이주호
'''

#변수 초기화
sum = 0
i = 0
switch = 1

##계산
for i in range(1, 100+1):
    #switch on
    if(switch == 1):
        sum = sum + i
        switch = 0
    #switch off
    elif(switch == 0):
        sum = sum - i
        switch = 1
##계산 종료

#결과 출력
print("1 - 2 + 3 - .. - 100 = %d" % (sum))
