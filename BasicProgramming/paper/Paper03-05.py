'''
<단순 변수 사용>
    3. 반복형
    3-5. 인구 계산 프로그램 (2020년 인구 4천 955만, 인구 증가율 - 0.02)
        - 이 때, 인구가 0 밑으로 떨어지는 년도는?
    1626035 이주호
'''

#변수 초기화
pop = 49550000      #인구
ratio = -0.02       #인구 증가율
n = 0               #2020년으로부터 지난 해 수

##계산
while(pop > 1):
    pop = pop + (pop * ratio)
    n = n + 1
##계산 종료

#결과 출력
print("인구가 1 밑으로 떨어지는 년도는 %d년입니다." % (2020 + n))
