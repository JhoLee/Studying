##기초프로그래밍 최종 레포트03


#출력문 최상단
title = ["이름", "국어", "영어", "수학", "총점", "평균", "석차"]

#이름 배열; 1번 주소부터 시작
name = ['', 'A', 'B', 'C', 'D', 'E']

#점수 배열
score = [
    [],
    [0, 82, 50, 70, 0, 0.0, 1],
    [0, 50, 60, 90, 0, 0.0, 1],
    [0, 40, 80, 50, 0, 0.0, 1],
    [0, 60, 70, 70, 0, 0.0, 1],
    [0, 70, 90, 80, 0, 0.0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

#총점 및 평균 계산
for i in range(1, 5+1):
    for j in range(1, 3+1):
        #총점 계산
        score[i][4] += score[i][j]
    #평균 계산
    score[i][5] = score[i][4] / 3

#석차 계산
for i in range(1, 5+1):
    for j in range(1, 5+1):
        if(score[i][4]<score[j][4]):
            score[i][6] += 1

#전체 총점 및 평균 계산
for i in range(1, 5+1):
    for j in range(1, 3+1):
        #총점 계산
        score[6][j] += score[i][j]
    for j in range(1, 3+1):
        # 평균 계산
        score[7][j] = float(score[6][j] / 5)

#출력문
for i in range(0, 7):
    print(title[i], end ="   ")
print()
for i in range(1, 5+1):
    print("   ", end="")
    #이름 출력
    print(name[i], end = "   ")
    #(국어~총점) 출력
    for j in range(1, 4+1):
        print("%4d"%score[i][j], end = "   ")
    #평균 출력
    print(" %2.1f"%float(score[i][5]), end = "  ")
    #석차 출력
    print("%5d"%score[i][6], end = "")
    print()
print("총점  ", end = "")
for j in range(1, 3+1):
    print("%5d"%score[6][j], end = "  ")
print()
print("평균   ", end = "")
for j in range(1, 3+1):
    print("%2.1f"%score[7][j], end = "   ")
print()
