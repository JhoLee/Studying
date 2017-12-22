####
#
# Title: Selection Search
#
# Date: 17.11.09
#
# by 1626035 / 이주호
#
# The algorithm for searching index of an element that has Kst small value
#
# Version for Using Function
#
# +) Set left value is a pivot
#
####

def Selection(A, k):

    left = 1
    right = len(A) - 1

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
            return A[j]



## main ##
if __name__ == "__main__":
    ## 배열1 ##
    arr1 = [0, 8, 3, 11, 9, 12, 2, 6, 15, 18, 10, 7, 14]
    n1 = len(arr1) - 1
    mid1 = Selection(arr1, n1 // 2)

    print("배열1 : ", end="")
    print(arr1[1:])
    print("원소의 수 : %d"% n1)
    print("중앙값 : %d" % mid1)
    print()


    ## 배열2 ##
    arr2 = [0, 8, 3, 11, 9, 12, 2, 6, 15, 18, 10, 7]
    n2 = len(arr2) - 1
    mid2 = Selection(arr2, n2 // 2)

    print("배열2 : ", end="")
    print(arr2[1:])
    print("원소의 수 : %d" % n2)
    print("중앙값 : %d" % mid2)
    print()
