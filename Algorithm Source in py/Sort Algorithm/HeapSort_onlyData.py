def maxHeap(array):
    n = len(array) - 1
    for i in range((n // 2), 0, -1):
        downHeap(array, i, n)

def downHeap(tree, i, n):
    biggest = i * 2
    while (biggest != i):
        if ((biggest + 1 <= n) and (tree[biggest + 1] > tree[biggest])):
            biggest = biggest + 1
        if ((biggest <= n) and (tree[biggest] > tree[i])):
            tree[biggest], tree[i] = tree[i], tree[biggest]
            i = biggest
            biggest = i * 2
        else:
            biggest = i

def heapSort(array):
    maxHeap(array)
    n = len(array) - 1
    while (n > 1):
        array[n], array[1] = array[1], array[n]
        n = n - 1
        downHeap(array, 1, n)

arr = [0, 7, 3, 5, 8, 6, 1, 6, 4]
print("Original Data")
print(arr[1:])
print()

heapSort(arr)

print("Sorted Data")
print(arr[1:])
print()
