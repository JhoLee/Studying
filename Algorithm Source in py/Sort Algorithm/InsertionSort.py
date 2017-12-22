# 0번 index의 값은 쓰지 않음.
arr = [0, 3, 1, 2, 5, 7, 1, 3, 5, 4, 2, 10, 8]


n = len(arr) - 1

for i in range(1, n + 1):
    temp = arr[i]
    j = i - 1
    while(j > 0 and arr[j] > temp):
        arr[j], arr[j+1] = arr[j+1], arr[j]
        j = j -1
    arr[j+1] = temp

print(arr[0:])



