##
# 연속 행렬 곱셈을 위한 동적 계획 알고리즘
#
# Date: 17.12.05
#
# Author: Jho
#
# +) '알고리즘(생능출판사)'의 p.151 참조.
#
# 입력: 연속된 행렬 A1 X A2 X ... X An
#       단, A1은 (d0 X d1), A2는 (d1 X d2), ..., An은 (dn-1 X dn) 이다.
#
# 출력: 입력의 행렬 곱셈에 필요한 원소 간의 최소 곱셉 횟수
#
# ++) 배열 생성 생략
#
##

from random import *

def minValue(a, b):
    if a > b is True:
        return a
    else:
        return b

# Define Infinity
INF = 999999999
##

# Generate n arrays
d = []  # List for arrays' length
n = 5   # Number of arrays

# Set Arrays' length in random integer (As 'd')
for i in range(0, n+2):
    d.append(randint(1, 9))


# Matrix Chain Algorithm
C = []
for i in range(0, n+2):
    C.append([])
    for j in range(0, n+2):
        C[i].append(0)
for L in range(1, n):
    for i in range(1, (n-L) + 1):
        j = i + L
        C[i][j] = INF
        for k in range(i, j):
            C[i][j] = minValue(C[i][j], C[i][k] + C[k+1][j] + d[i - 1] * d[k] * d[j])
##

# Output
for i in range(0, n):
    print("A%d" % i, end="")
    print("(%d X %d) " % (d[i], d[i + 1]), end="\t")
print()

print("Array C..")
for i in range(1, n+1):
    for j in range(1, n+1):
        print("%5d" % C[i][j], end="")
    print()
print("Answer: %d" % C[1][n])
##