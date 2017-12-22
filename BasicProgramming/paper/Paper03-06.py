'''
<단순 변수 사용>
    3. 반복형
    3-6. 구구단 출력 (수직 출력, 수평 출력)
    1626035 이주호
'''

#변수 초기화
i = 0
j = 0

##출력
#수직 출력
print("수직 출력")
for j in range(1, 9+1):
    for i in range(1, 9+1):
        print("%d X %d = %d\t" % (i, j, i*j), end = "")
    print()
print()
#수평 출력
print("수평 출력")
for i in range(1, 9+1):
    for j in range(1, 9+1):
        print("%d X %d = %d\t" % (i, j, i*j), end = "")
    print()
##출력 종료