####
#
# Title: Selection Search
#
# Date: 17.11.13
#
# by 1626035 / 이주호
#
# The algorithm for searching index of an element that has Kst small value
#
# Version for using no function
#
# +) Set left value is a pivot
#
####

A = [None, 8, 3, 11, 9 ,12, 2, 6, 15, 18, 10, 7, 14]
print("원 배열 : ", end="")
print(A[1:])
print("배열 원소의 수 : %d" % (len(A) - 1))
print()

k = 6

left = 1
right = 12

hStack = [] # Stack for High Index
lStack = [] # Stack for Low index

lStack.append(left)
hStack.append(right)

## While Stack is not Empty ##
while(lStack != [] and hStack != []):
    m = lStack.pop()
    n = hStack.pop()

    # Let 'pivot' <- A[m]
    i = m + 1
    j = n

    while (i < j):
        while (i < n and A[i] < A[m]):
            i = i + 1

        while ( j > m and A[j] > A[m]):
            j = j - 1

        if (i < j):
            A[i], A[j] = A[j], A[i]

    if(A[j] < A[m]):
        A[j], A[m] = A[m], A[j]

    # j == k
    if(j > k):
        lStack.append(m)
        hStack.append(j - 1)
    elif (j < k):
        lStack.append(j + 1)
        hStack.append(n)
    else:
        print("%d번째로 작은 값은 %d 입니다." % (k, A[j]))








