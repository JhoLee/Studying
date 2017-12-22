R = [8, 3, 11, 9, 12, 2, 6, 15, 18, 10, 7, 14]
stack = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
top = 0
m = 0
n = 11

top += 1
stack[0][top] = m
stack[1][top] = n

while(top > 0):

    m = stack[0][top]
    n = stack[1][top]
    top -= 1
    i  = m + 1
    j = n

    while(i<j):
        while(i <= n and R[i] < R[m]):
            i = i + 1
        while(j > m and R[j] > R[m]):
            j = j - 1
        if(i < j):
            R[i], R[j] = R[j], R[i]
    if(R[j] < R[m]):
        R[m], R[j] = R[j], R[m]
    print(R)
    if ( (j-1) > m):
        top += 1
        stack[0][top] = m
        stack[1][top] = (j - 1)
    if( (j+1) < n):
        top += 1
        stack[0][top] = j+1
        stack[1][top] = n
print(R)