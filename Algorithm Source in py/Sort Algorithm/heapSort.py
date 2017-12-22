array = [0, 5, 26, 37, 1, 61, 11, 59]

print ("입력데이터 = """, end = "")
for i in range (1, 8, 1) :
    print("%3d" % array[i], end = " ")
print()

rt_cnt = 0

for loop in range (7, 0, -1):

    rt_cnt = rt_cnt + 1

    for i in range (int(loop/2), 0, -1):
        rtemp = array[i]
        j = 2 * i
        while (j<= loop):
            if (j<loop and array[j]<array[j+1]):
                j = j + 1
            if (rtemp < array[j]):
                array[int(j/2)] = array[j]
                j = 2 * j
            else:
                break
            array[int(j/2)] = rtemp

        print()
        print("%3d 회전 = " % rt_cnt, end=" ")
        for i in range(1, 8, 1):
            print("%3d" % array[i], end=" ")
    print ()
    print ("%3d 회전 = " % rt_cnt, end = " ")
    for i in range(1, 8, 1):
        print ("%3d" % array[i], end = " ")

    atemp = array[1]
    array[1] = array[loop]
    array[loop] = atemp
    print ()
    print ("%3d 교환 = " % rt_cnt, end = " ")
    for i in range (1, 8, 1):
        print ("%3d" % array[i], end = " ")
    print ()

print ()
print("최종결과 = " , end = " ")
for i in range (1, 8, 1):
    print ("%3d" % array[i], end = " ")
