###
#
# Quick Sort - Iterative version
#
# 17.11.03
#
# by 1626035, Joo-Ho Lee
#
###

## main ##
arr = [None, 8, 3, 11, 9, 12, 2, 6, 15, 18, 10, 7, 14]
print('Original Data is.. ')
print(arr[1:])
print()

m = 1
n = 12

hStack = []  # Stack for High Index
lStack = []  # Stack for Low Index

lStack.append(m)
hStack.append(n)

## While Stack is not empty ##
while (lStack != [] and hStack != []):
    ## R[m:n]에 대한 정렬 시작 ##
    m = lStack.pop()
    n = hStack.pop()

    # Let 'pivot' <- R[m]
    i = m + 1
    j = n
    while (i < j):
        while (i <= n and arr[i] < arr[m]):
            i = i + 1

        while (j > m and arr[j] > arr[m]):
            j = j - 1

        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]

    if (arr[j] < arr[m]):
        arr[j], arr[m] = arr[m], arr[j]

    ##  R[i]를 기준으로, 두 배열로 나뉨.
    # 정리해야 할 부분의 index를 stack에 저장.
    if (m != j and (j - 1) > m):
        lStack.append(m)
        hStack.append(j - 1)
    if ((j + 1) < n and n != j):
        lStack.append(j + 1)
        hStack.append(n)
## If (Stack is empty), End of loop ##

print('Sorting Finished.')
print(arr[1:])
print()