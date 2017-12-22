"""
    책에 나온 알고리즘 구현
    P.216~221, 336~347
"""

## BuildHeap; 배열 'array'를 Heap으로 만듬
def buildHeap(array, n):
    for i in range(n//2, 1+1):
        print(array)
        downHeap(array, n, i)


## DownHeap
def downHeap(array, n, i):
    leftChild = (i * 2)
    rightChild = (i * 2) +1
    if ((leftChild<=n) & (array[leftChild]>array[i])): # n은 원소의 수
        bigger = leftChild
    else:
        bigger = i
    if ((rightChild<=n) and (A[rightChild]>array[bigger])):
        bigger = rightChild
    if (bigger != i):
        # swap
        temp = array[i]
        array[i] = array[bigger]
        array[bigger] = temp

    print(array)
    downHeap(array, n, i)


## Main
arr = [0, 2, 31, 2, 4, 2, 45, 23]
buildHeap(arr, 7)
