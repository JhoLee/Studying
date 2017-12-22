ar = [8, 8, 11, 9, 12, 2, 6, 15, 18, 10, 7, 14]
stack = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
m = 0
n = 11
i = m + 1
j = n
top =1

while(top!= 0):
    top = 0
    ## 원문
    # while(top != 0):
    while(j>=i):
        ## 원문
        # while(ar[i] <= ar[m]):
        while(i <= n and ar[m] > ar[i]):
            i += 1
        ## 원문
        # while(ar[i] >= ar[m]):
        while(j > m and ar[m] < ar[j]):
            j -= 1
        if (i < j):
            temp = ar[j]
            ar[j] = ar[i]
            ar[i] = temp
        else:
            break
        ## 원문
        # temp = ar[j]
        # ar[i] = ar[m]
        # ar[m] = temp

    temp = ar[i]
    ar[i] = ar[m]
    ar[m] = temp
    print(ar)
    print("\n")

    ##stack insert
    top+=1
    ## 원문
    # stack[0][top] = j+1
    # stack[1][top] = m
    if(i+1 < n):
        stack[0][top] = i + 1
        stack[1][top] = n
    top += 1
    ## 원문
    # stack[0][top] = n
    # stack[1][top] = j - 1
    if(i -1 > m):
        stack[0][top] = m
        stack[1][top] = i -1

    ## stack delete
    m = stack[0][top]
    n = stack[1][top]
    top -= 1