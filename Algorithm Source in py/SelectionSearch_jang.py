arr=[8,3,11,9,12,2,6,15,18,10,7,14]
left=0
right=len(arr)-1
key_position=key=3

print("입력 자료 ㅂㅐ열 = ",arr)
print("key position = %2d " % key)
print("pivot position = %2d" %(left))
print()

while(True):

    pivot = left
    r=right

    while(l<r):
        while(arr[l]<=arr[pivot] and l<right):
            l=l+1
        while(arr[r]>=arr[pivot] and l>left):
            r=r-1
        if(l<r):
            arr[l],arr[r] = arr[r],arr[l]
        print("자료 교환 과정 :   ㅣ=%2d  r = %2d  " %(l,r),end="")
        print(arr)
    arr[pivot],arr[r] = arr[r],arr[pivot]
    print("피복 교환 과정 : pivot = %2d r = %2d  " %(pivot,r),end="")
    print(arr)

    s = (r-1) -left +1
    print("key index key = %2d  " %key,end="")
    print("small group의 크기 s = %2d  " %s,end="")
    print("small group과 pivot 을 포함한 크기 s+1 = %2d" %(s+1))
    print()

    if(key <=s):
        right = r-1
    else:
        if(key==s+1):
            print()
            print("%d번째 자료 = " %key_position,end="")
            print(arr[r])
            break
        else:
            left = r+1
            key=key-s-1
