## Array를 MaxHeapTree 로 정리
def maxHeap(array):
    n = len(array) - 1
    for i in range((n//2), 0, -1):
        downHeap(array, i, n)
    print("finished")
    print(array)
    print()



## MaxHeap 규칙대로 정리
def downHeap(tree, i, n):
    bigger = i
    while(1): # 수정 예정
        # 정리 조건
        print("주소: %d  값 : %d" %(i, tree[i]))
        if( ((i * 2) <= n) and (tree[i*2] > tree[bigger]) ):
            # LeftChild > Parent
            bigger = i * 2
            print("left")

        if( ((i*2)+1 <= n) and (tree[(i*2)+1] > tree[bigger]) ):
            # RightChild > Parent
            bigger = (i * 2) + 1
            print("right")

        # swap
        if(bigger != i):
            tree[bigger], tree[i] = tree[i], tree[bigger]
            i = bigger
            print(tree)
            print()
        else:
            print("parent")
            print(tree)
            print()
            break


## 오름차순 Heap Sort
def ascendHeapSort(array):
    maxHeap(array)
    print("ascendHeapSort")
    print(array)
    n = len(array) - 1
    count = 0
    while(n>1):
        print("Sorting..")
        count = count + 1
        print("count: %d; n: %d" % (count, n))
        array[n], array[1] = array[1], array[n]
        n = n - 1
        print(array)
        downHeap(array, 1, n)
        print(array)



## Main

arr = [0, 3, 5, 8, 7, 1, 2, 6, 4]
print("초기" )
print(arr)
print("시작")
print()
ascendHeapSort(arr)

print()
print("끝")
print(arr)
print()