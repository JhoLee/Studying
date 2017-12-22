def findMax(tree, P):
    temp = tree[P]
    L = (P * 2)
    R = (P * 2) + 1
    if (tree[L] > tree[R]):
        if (tree[L] > tree[P]):
            # L.key > P.key
            return L
    if (tree[R] > tree[P]):
            # R.Key > P.key
            return R
    else:
        return P


def buildHeap(array, n):
    tree = [0]
    for i in range(1, n+1):
        print(tree)
        tree = heapInsertion(tree, len(tree), array[i])


def heapInsertion(tree, n, value):
    tree.append(value)
    print(tree)
    for j in range(n//2, 1-1, -1):
        now = j
        while(max(j, j*2, j*2+1) != now):
            temp = tree[max(j, j*2, j*2+1)]
            tree[max(j, j*2, j*2+1)] = tree[j]
            tree[j] = temp
    return tree



buildHeap([0, 4, 234, 2, 3, 1, 2, 5, 6, 2, 3], 10)