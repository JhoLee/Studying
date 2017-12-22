####
#
# Title: Selection Search
#
# Date: 17.11.14
#
# by 1626035 / 이주호
#
# The algorithm for searching index of an element that has Kst small value
#
# Version for Using Function
#
# +) Set pivot in random
#
####
import random

def Selection(A, left, right, k):

    # Making Stacks #
    lStack = [] # A stack for left index
    rStack = [] # A stack for right index
    kStack = [] # A stack for k index
    # EMS #

    lStack.append(left)
    rStack.append(right)
    kStack.append(k)

    ## Using 'while' to avoid using recursion
    ## Start of Loop ##
    while lStack != [] and rStack != [] and kStack != [] :

        left = lStack.pop()
        right = rStack.pop()
        k = kStack.pop()

        # Set pivot index in random
        pivot = random.randrange(left, right + 1)

        # Swap A[left] <-> A[pivot]
        A[left], A[pivot] = A[pivot], A[left]

        pivot = left
        i = pivot + 1
        j = right

        while i < j:
            while i < right and A[i] < A[pivot]:
                i = i + 1

            while j > left and A[j] > A[pivot]:
                j = j - 1

            if i < j:
                A[i], A[j] = A[j], A[i]


        if(A[j] < A[pivot]):
            A[j], A[pivot] = A[pivot], A[j]

        pivot = j

        # S means 'size of a small group'
        S = (pivot - 1) - left + 1

        ## Search in small group
        if k <= S:
            lStack.append(left)
            rStack.append(pivot - 1)
            kStack.append(k)

        ## pivot == k
        elif k == S + 1 :
            return A[pivot]

        ## Search in large group
        else:
            lStack.append(pivot + 1)
            rStack.append(right)
            kStack.append(k - S - 1)
     ## End of Loop ##



## main ##
if __name__ == "__main__":
    ## 배열1 ##
    arr1 = [0, 8, 3, 11, 9, 12, 2, 6, 15, 18, 10, 7, 14, 13]
    print("배열1 : ", end="")
    print(arr1[1:])

    n1 = len(arr1) - 1
    mid1 = Selection(arr1, 1, n1, n1 // 2)

    print("원소의 수 : %d"% n1)
    print("중앙값 : %d" % mid1)
    print()

