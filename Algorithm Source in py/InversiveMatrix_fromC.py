"""
 역행렬 프로그램 (C에서 변환)
"""

# 기준 배열 길이
n = 3

## 배열 hang값의 교환 위한 임시방인 temp의 실수 값의 소수값의 확대 위해 double 선언
hang_1 = [
    [1, -1, 2],
    [3, 0, 1],
    [1, 0, 2]
]

# 모든 원소 값이 0인, 'n X 2n' 행렬 선언
hang_2 = []
for i in range(0, n):
    hang_2.append([])
    for j in range(0, n*2 ):
        hang_2[i].append(0)

## 배열 hang2로 초기 값 입력
for i in range(0, n):
    for j in range(0, n):
        hang_2[i][j] = hang_1[i][j]

## 주어진 행렬의 뒷부분에 단위행렬 입력
for i in range (0, n):
    for j in range(0, n):
        if(i==j):
            hang_2[i][j+n] = 1
        else:
            hang_2[i][j+n] = 0

## Gaussian Elimination 알고리즘
for i in range(0, n):
    ## 피봇 행 처리
    temp = hang_2[i][i]
    for j in range(0, (n*2)):
        hang_2[i][j] = hang_2[i][j] / temp
    for k in range(0, n):
        ## 피봇 행을 제외한 나머지 행의 열부분 zero화 처리
        if(i!=k):
            temp = hang_2[k][i]
            for j in range(0, (n * 2)):
                hang_2[k][j] = hang_2[k][j] - (hang_2[i][j] * temp)

## 주어진 행렬의 변환된 단위 행렬과 역행렬 결과 출력
for i in range(0, n):
    for j in range(0, (n * 2), 1):
        print("%6.1f\t" % hang_2[i][j], end="")
    print()
print()

###################################
## 여기까지가 주어진 소스의 변환 ##
###################################

## 원시행렬 출력
print("원시행렬")
for i in range(0, n):
    for j in range(0, n):
        print("%6.1f\t" % hang_1[i][j], end="")
    print()
print()

## 단위 행렬과 역행렬이 합쳐진 행렬로부터, hang3에 역행렬 추출
hang_3 = []

for i in range(0, n, 1):
    hang_3.append(hang_2[i][n:])

## 원시행렬의 역행렬 출력
print("원시행렬의 역행렬")
for i in range(0, n, 1):
    for j in range(0, n, 1):
        print("%6.1f\t" % hang_3[i][j], end="")
    print()
print()


## 원시행렬과 역행렬의 곱셈 ##

# 결과를 더할 행렬
hang_4 = []
for i in range(0, n):
    hang_4.append([])
    for j in range(0, n):
        hang_4[i].append(0)

## 곱셈 시작
for i in range(0, n):
    for j in range(0, n):
        for k in range(0, n):
            hang_4[i][j] += (hang_1[i][k] * hang_3[k][j])

## 결과 행렬 출력
print("원시행렬 X 역행렬 결과...")
for i in range(0, n):
    for j in range(0, n):
        print("%6.1f\t" % hang_4[i][j], end="")
    print()
print()