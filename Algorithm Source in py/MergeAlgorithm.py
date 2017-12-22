"""
1626035 / 이주호
"""
## 배열
A = [20, 30, 40, 50]
B = [25, 35, 55, 60, 70]
C = [0, 0, 0, 0, 0, 0, 0, 0, 0]

## Merge
nA = len(A)
nB = len(B)
nC = len(A) + len(B)

i = 0   # Index of  A
j = 0   # Index of B
k = 0   # Index of C

while( i < nA and j < nB ):
    if( A[i] < B[j]):
        C[k] = A[i]
        i = i + 1
        k = k + 1

    else:
        C[k] = B[j]
        j = j + 1
        k = k + 1

if( i < nA ):
    C[k:] = A[i:]
else:
    C[k:] = B[j:]

## Print
print("arr A: ", end = "")
print(A)
print("arr B: ", end = "")
print(B)
print("arr C: ", end = "")
print(C)