### Examples of Sorts ###
## Original Bubble Sort
def bubbleSort01(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) - (i+1)):
            if (array[j] > array[j + 1]):
                array[j], array[j+1] = array[j+1], array[j]
    return array
##


## Modified Bubble Sort
def bubbleSort02(array):
    k = len(array)
    flag = 1
    while (flag):
        k = k - 1
        flag = 0
        for j in range(0, k):
            if (array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
                flag = 1
    return array
##


## Selection Sort
def selectionSort(array):
    for i in range (0, len(array) - 1):
        for j in range (i + 1, len(array)):
            if (array[i] > array[j]):
                array[i], array[j] = array[j], array[i]
    return array
##

## End of Sorts by Swapping ##

## Qucik Sort ##
# Skip for this time


## Heap Sort
def maxHeap(array, n):
    for i in range( (n-1) // 2, -1, -1):
        j = i
        k = (j * 2) + 1
        biggest = k
        while(biggest < n and j != biggest):
            if(k+1 < n and array[k+1] > array[biggest]):
                biggest = k+1
            if(array[j] > array[biggest]):
                biggest = j
            if(j != biggest):
                array[j], array[biggest] = array[biggest], array[j]
                j = biggest
                k = (j * 2) + 1
                biggest = k

    return array


def heapSort(array):
    n = len(array)
    array = maxHeap(array, n)
    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        array = maxHeap(array, i)
    return array
##


## Insertion Sort
def insertionSort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while( j >= 0 and array[j] > temp):
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = temp
    return array
##


## Shell Sort
def shellSort(array, gap):
    for h in gap:
        for i in range(h, len(array)):
            temp = array[i]
            j = i - h
            while( j>= 0 and array[j] > temp):
                array[j+h] = array[j]
                j = j - h
            array[j+h] = temp
    return array
##
### End of Sorts ###

### Validation ###
## Generates a random array ##
def randArray(n):
    import random
    array = []
    for i in range(0, n):
        array.append(random.randrange(0, 100))
    return array


## Main
n = 10
array = randArray(n)
print()

arrays = []
for i in range(0, 6):
    arrays.append(randArray(n))
print("Bubble 01")
print(arrays[0])
print(bubbleSort01(arrays[0]))
print()
print("Bubble 02")
print(arrays[1])
print(bubbleSort02(arrays[1]))
print()
print("Selection")
print(arrays[2])
print(selectionSort(array))
print()
print("Heap")
print(arrays[3])
print(heapSort(arrays[3]))
print()
print("Insertion")
print(arrays[4])
print(insertionSort(arrays[4]))
print()
print("Shell")
print(arrays[5])
print(shellSort(arrays[5], range(n, 0, -1)))
print()
print("End of File")