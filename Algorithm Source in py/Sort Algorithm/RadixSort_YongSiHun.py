arr=[89,70,35,131,910]

print("원 배열")
for i in range(0,5,1):
    print(arr[i],end="  ")
print("\n")

for i in range(0,5,1):
    for j in range(0,5,1):
        if (arr[i]%10<arr[j]%10):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("1의 자리 순서정렬")
for i in range(0,5,1):
    print(arr[i],end="  ")
print("\n")

for i in range(0,5,1):
    for j in range(0,5,1):
        if int(arr[i]%100)/10<int(arr[j]%100)/10:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("10의 자리 순서정렬")
for i in range(0,5,1):
    print(arr[i],end="  ")
print("\n")

for i in range(0,5,1):
    for j in range(0,5,1):
        if int(arr[i]%1000)/100<int(arr[j]%1000)/100:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("100의 자리 순서정렬")
for i in range(0,5,1):
    print(arr[i],end="  ")
print("\n")