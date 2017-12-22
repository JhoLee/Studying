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
    [0, 1, 0, 3],
    [7, 0, 0, 0],
    [0, 4, 5, 0],
    [5, 0, 1, 6]
]
n = len(a[0])
print("원시 행렬 (%d x %d)" % (n, n))
printMatrix(a)


## step 1) 주어진 행렬에 같은 크기의 단위 행렬 추가
for i in range(0, n):
    for j in range(0, n):
        if (i == j):
            a[i].append(1)
        else:
            a[i].append(0)
print("주어진 행렬에 같은 크기의 단위 행렬 추가")
printMatrix(a)


## step 2 ~ 4
for i in range(0, n):
    for j in range(0, n):
        if((i != j) and a[i][i] != 0):
            if (a[i][i] != 1):
                rValue = a[i][i]
                for m in range(0, n * 2):
                    a[i][m] = a[i][m] / rValue
            rValue = a[j][i] / a[i][i]
            for m in range(0, n * 2):
                a[j][m] = a[j][m] - a[i][m] * rValue

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


## 최종 결과
print("최종 결과")
printMatrix(a)