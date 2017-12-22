##
#
# Title: Quick Selection Algorithm in Swap
# Date: 17.12.10
# Author: 1626035
#
##

def QuickSelect(A):
    print("배열: ", A[1:])

    left = 1
    right = len(A) - 1

    print("몇번째로 작은 값을 찾을까요 >> ", end="")
    key = int(input())

    hStack = []  # Stack for High Index
    lStack = []  # Stack for Low Index

    lStack.append(left)
    hStack.append(right)

    while ((lStack is not []) and (hStack is not [])):
        # While Stack is not Empty #
        m = lStack.pop()
        n = hStack.pop()

        # 'pivot' <- A[m]
        i = m + 1
        j = n
        while i < j:
            while (i < n) and (A[i] < A[m]):
                i = i + 1
            while (j > m) and (A[j] > A[m]):
                j = j - 1
            if i < j:
                A[i], A[j] = A[j], A[i]

        if A[j] < A[m]:
            A[j], A[m] = A[m], A[j]

        if j > key:
            lStack.append(m)
            hStack.append(j - 1)
        elif j < key:
            lStack.append(j + 1)
            hStack.append(n)
        else:
            print("주어진 배열 ", A[1:])
            print("에서 %d번째로 작은 값은, %d입니다. " % (key, A[j]))
            return


# Main
if __name__ == "__main__":
    arr = [None, 8, 3, 11, 9, 12, 2, 6, 15, 18, 10, 7, 14]

    QuickSelect(arr)
