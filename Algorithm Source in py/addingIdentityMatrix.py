## Shell Sort

# 원시배열
arr = [30, 60, 90, 10, 40, 80, 40, 20, 10, 60, 50, 30, 40, 90, 80]
print("원시배열" )
print(arr)
print()

# 매개변수 gap -> (5, 3, 1)
gap = [5, 3, 1]
print("매개변수")
print(gap)
print()

# 정렬 시작
for h in gap:
        print("현재 매개변수 : %d " % (h))
        print()
        for i in range(h, len(arr)):
            temp = arr[i]
            j = i
            print("\t", end="")
            print(arr)
            print("\t%d번째 값 \'%d\' -> " % (i+1, temp), end="")
            while((j >= h) and (arr[j-h] > temp)):
                arr[i] = arr[j-h]
                j = j-h
            arr[j] = temp
            print("%d번째에 삽입" % (j+1))
            print("\t", end="")
            print(arr)
            print()
        print()
print("정렬 완료")
print(arr)