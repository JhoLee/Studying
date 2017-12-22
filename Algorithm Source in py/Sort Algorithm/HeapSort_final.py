## Array를 MaxHeap 로
def maxHeap(array):
    n = len(array) - 1
    for i in range((n // 2), 0, -1):
        downHeap(array, i, n)


## MaxHeap 규칙대로 정리
def downHeap(tree, i, n):
    biggest = i * 2  # 초기에는 i번 노드의 LeftChild 값
    while (biggest != i):
        if ((biggest + 1 <= n) and (tree[biggest + 1] > tree[biggest])):
            # RightChild > LeftChild
            biggest = biggest + 1
        if ((biggest <= n) and (tree[biggest] > tree[i])):
            # (LeftChild or RightChild) > Parent
            tree[biggest], tree[i] = tree[i], tree[biggest]  # biggest <-> Parent
            # 바꿔준 자노드의 자리에서부터 다시 힙 규칙 검사 시작
            i = biggest
            biggest = i * 2
        # (Parent > RightChild) & (Parent > LeftChild)
        else:
            biggest = i
        print(tree[1:])


## 오름차순 Heap Sort
def heapSort(array):
    print("Making a Heap..")
    maxHeap(array)
    print()
    print("MaxHeap")
    print(array[1:])
    print()
    print("Sorting Start..")
    n = len(array) - 1
    while (n > 1):
        array[n], array[1] = array[1], array[n]
        n = n - 1
        downHeap(array, 1, n)
        print()
    print("Sorting finished.")
    print()


## Main
arr = [0, 7, 3, 5, 8, 6, 1, 6, 4]
print("Original Data")
print(arr[1:])
print()

heapSort(arr)

print("Sorted Data")
print(arr[1:])
print()
