## 문제 제공 내용

# 본 프로그램은 Radix Sort에서K1의 자리부터 K2 윗자리로 올라가는 LSD 우선 ( Least Significant Digit First)방식으로 처리
# 큐는 총 10개로 되어있으며, 각 10단위에서 두 개의 데이터가 들어갈 수 있도록 버켓의 크기를 잡아줌
radix_queue = [[], [], [], [], [], [], [], [], [], []]
# 입력데이터는 1과 10의 자리 두자리로 된 데이터, 10단위에서 각각 두 개씩 사용
data = [15, 23, 31, 49, 58, 64, 72, 80, 96, 7, 5, 93, 81, 79, 68, 54, 42, 30, 26, 17]
# 10의 자리에 대한 모듈러값을 계산하기 위해 임시로 잡아준 데이터 배열 변수
var_data =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

## 문제 제공 내용 끝



print("입력 자료")
print(data)
print()

# variables
check = 0
count = 1
n = len(data)
while(check != 1):

    while(len(data) != 0):


        num = data.pop(0)
        modValue = num // (pow(10, count-1))
        modValue = modValue % (pow(10, count))
        radix_queue[modValue].append(num)

    ## "Kn 정렬 큐 상태" 출력
    print("K%d 정렬 큐 상태" % count)
    for i in range(0, 10):
        print("큐%d " % i, end = "")
        for j in range(0, len(radix_queue[i])):
            print("%3d" % radix_queue[i][j], end="")
        print()
    print()
    ## "Kn 정렬 큐 상태" 출력 끝

    if (len(radix_queue[0]) == n):
        check = 1

    for i in range(0, 10):
        while(len(radix_queue[i]) != 0):
            data.append(radix_queue[i].pop(0))

    ## "Kn 정렬 자료" 출력
    print("K%d 정렬 자료" % count)
    print(data)
    print()
    ## "Kn 정렬 자료" 출력 끝

    count = count + 1







