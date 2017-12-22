##
#
# Title: Quick Sort
#
# Date: 17.11.03
#
# by 1626035, Joo-Ho Lee
#
# ps) 유인물 <Divide & Conquer 분할 및 정복> 6페이지의 Data set 사용
#
##


def quickSort(R):

    m = 0
    n = len(R) - 1

    hStack = [] # Stack for High Index
    lStack = [] # Stack for Low Index

    print('push (%d, %d) into stack' % (m, n))
    lStack.append(m)
    hStack.append(n)

    ## While Stack is not empty ##
    while (lStack != [] and hStack != []):
        ## R[m:n]에 대한 정렬 시작 ##
        m = lStack.pop()
        n = hStack.pop()
        print('pop (%d, %d) from stack ' % (m, n))
        print('m = %d n = %d' % (m, n))
        print()

        # Let 'pivot' <- R[m]
        i = m + 1
        j = n
        while (i < j):
            while (i < n and R[i] < R[m]):
                i = i + 1

            while (j > m and R[j] > R[m]):
                j = j - 1

            if (i < j):
                R[i], R[j] = R[j], R[i]
                print('swap arr[i] and arr[j]')
                print('m = %d n = %d i = %d j = %d' % (m, n, i, j))
                print(R)
                print()
        if (R[j] < R[m]):
            R[j], R[m] = R[m], R[j]
            print('swap arr[m] and arr[j]')
            print('m = %d n = %d i = %d j = %d' % (m, n, i, j))
            print(R)
            print()

        ##  R[i]를 기준으로, 두 배열로 나뉨.
        # 정리해야 할 부분의 index를 stack에 저장.
        if (m != j and (j - 1) > m):
            print('push (%d, %d) into stack' % (m, j - 1))
            lStack.append(m)
            hStack.append(j - 1)
        if ((j + 1) < n and n != i):
            print('push (%d, %d) into stack' % (j + 1, n))
            lStack.append(j + 1)
            hStack.append(n)
    ## If (Stack is empty), End of loop ##


    print('Sorting Finished.')
    print(R)
    return R


## main ##
if __name__ == "__main__":
    arr = [8, 3, 11, 9, 12, 2, 6, 15, 18, 10, 7, 14]
    print(arr)
    print()
    quickSort(arr)

