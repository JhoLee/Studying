def findMidValue(A, n):
    print("원 배열 : ", end = "")
    print(A[1:])
    print("원소의 개수 : %d" % n)
    print()

    ## 정렬 과정 생략
    A.sort()

    ## 중앙값 도출
    # 홀수개인 경우 #
    if (n % 2 == 1):
        k = n // 2
        print("중앙값은 %d 입니다." % A[k+1])
        print()

    # 짝수개인 경우 #
    else:
        k = n // 2
        print("중앙값은 %.2f 입니다." % ((A[k]+A[k+1])/2.0))
        print()


## 배열1 ##
arr1 = [0, 8, 3, 11, 9, 12, 2, 6, 15, 18, 10, 7, 14]
n1 = len(arr1) - 1
findMidValue(arr1, n1)

## 배열2 ##
arr2 = [0, 8, 3, 11, 9, 12, 2, 6, 15, 18, 10, 7]
n2 = len(arr2) - 1
findMidValue(arr2, n2)