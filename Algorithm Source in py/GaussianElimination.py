def printMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if(matrix[i][j] % 1 == 0):
                print("%7d" % matrix[i][j], end = "")
            else:
                print("%7.2f" % matrix[i][j], end = "")
        print()
    print()


## 원시 행렬 (3 X 3)
a = [
    [1, -1, 2],
    [3, 0, 1],
    [1, 0, 2]
]
n = len(a[0])
print("원시 행렬 (%d x %d)" % (n, n))
printMatrix(a)


## step 1) 주어진 행렬에 같은 크기의 단위 행렬 추가
#   - 원시행렬이 단위 행렬로 바뀔 수 있도록 소거 작업 실시
for i in range(0, n):
    for j in range(0, n):
        if (i == j):
            a[i].append(1)
        else:
            a[i].append(0)
print("주어진 행렬에, 같은 크기의 단위 행렬 추가")
printMatrix(a)


## step 2 ~ 4
for i in range(0, n):
    print("%d행을 피벗 행으로 하여, 다른 행의 %d열을 소거" % (i+1, i+1))
    for j in range(0, n):
        if((i != j) and a[i][i] != 0):
            if (a[i][i] != 1):
                # 기준 값이 1이 아닌 경우
                rValue = a[i][i]
                for m in range(0, n * 2):
                    a[i][m] = a[i][m] / rValue
            rValue = a[j][i] / a[i][i]
            for m in range(0, n * 2):
                a[j][m] = a[j][m] - a[i][m] * rValue
        printMatrix(a)
    print("%d회전 결과" % (i + 1))
    printMatrix(a)
    print()

## 완료 검증
for i in range(0, n):
    if(a[i][i] != 1):
        for j in range(0,n):
            if ((i != j) and a[i][i] != 0):
                if (a[i][i] != 1):
                    rValue = a[i][i]
                    for m in range(0, n * 2):
                        a[i][m] = a[i][m] / rValue
                rValue = a[j][i] / a[i][i]
                for m in range(0, n * 2):
                    a[j][m] = a[j][m] - a[i][m] * rValue
        print("실행되지 않은, %d행에 의한 소거 재실행" % (i+1))
        printMatrix(a)
        print()



## 최종 결과
print("최종 결과")
printMatrix(a)