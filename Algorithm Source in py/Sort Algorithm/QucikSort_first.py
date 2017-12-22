"""
 김용승 교수님의 알고리즘을 그대로 구현
"""
def QuickSort(R, m, n):
    if(m < n):
        i = m
        j = n + 1

        while(1):
            while(i < len(R) and R[i]>=R[m]):
                i =i + 1
            while(j < len(R) and R[j]<=R[m]):
                j = j - 1
            if (i < j):
                R[i], R[j] = R[j], R[i]
            else:
                break
    R[m], R[j] = R[j], R[m]
    QuickSort(R, m, j-1)
    QuickSort(R, j+1, n)

    return R


R = [2, 4, 2, 1, 4]

print(R)

print(QuickSort(R, 0, len(R)))