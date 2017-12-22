'''
<단순 변수 사용>
    2. 선택형
    2-3. 점수의 등급 계산 (A, B, C, D, F)
    1626035 이주호
'''

#점수 입력
score = int(input("점수 입력(0~100) >> "))

#등급 계산
if(score > 100):
    print("점수 범위 초과")
if(score < 0):
    print("점수 범위 초과")
if(score >= 90):
    print("%d점은 A입니다." % score)
elif(score >= 80):
    print("%d점은 B입니다." % score)
elif(score >= 70):
    print("%d점은 C입니다." % score)
elif(score >= 60):
    print("%d점은 D입니다." % score)
elif(score >= 0):
    print("%d점은 F입니다.")
