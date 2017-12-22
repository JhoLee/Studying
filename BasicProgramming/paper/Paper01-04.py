'''
<단순 변수 사용>
    1. 순차형
    1-4. 초를 시분초로 환산
    1626035 이주호
'''

#계산할 초 입력
seconds = int(input("환산할 초를 정수로 입력 >> "))

##시간 계산
#시
hour = seconds / (60 * 60)
#분
minute = seconds % (60 * 60)
minute = minute / 60
#초
sec = seconds % 60
##시간 계산 종료

#결과 출력
print("%d초는 %d시간 %d분 %d초 입니다." % (seconds, hour, minute, sec))