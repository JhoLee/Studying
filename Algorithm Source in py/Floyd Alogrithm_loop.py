##
#
# Floyd Algorithm - loop
#
# Author: Jho
#
# date: 17.12.08
#
#
# +) 'Floyd Algorithm'을 여러 번 반복함으로써,
#       여러 번 우회한 경로에 대한 결과를 얻을 수 있는지
#       검증하기 위한 프로그램
#
##
M = 99

def print_array(array):
    """
    Function for printing array in matrix.
    :param array: The array which you want to print out.
    :return: void
    """
    _arr = array
    m = len(_arr)
    n = len(_arr[0])
    for i in range(0, m):
        for j in range(0, n):
            print("%5d" % _arr[i][j], end="")
        print()
    print()
    return

def floyd_algorithm(array):
    """
    :param array: The array of graph which you want to adapt 'Floyd Algoritm'.
    :return: The array after adapting floyd algorithm.
    """

    _arr = array
    n = len(_arr)
    print("Original array")
    print_array(array)
    for k in range(0, n):
        print("k = ", k)
        for i in range(0, n):
            for j in range(0, n):
                if (i is not k) and (j is not k):
                    _arr[i][j] = min(_arr[i][j], (_arr[i][k] + _arr[k][j]))
        print_array(_arr)
        print()

    return _arr


if __name__=="__main__":
    arr = [
        [0, 8, M, 1],
        [M, 0, 1, M],
        [4, M, 0, M],
        [M, 2, 9, 0]
    ]

    testing = [
        [0, 15, 1, M],
        [M, 0, M, M],
        [M, M, 0, 2],
        [M, 3, M, 0]
    ]

    testing2 = [
        [0, 3, M, M],
        [M, 0, M, M],
        [2, M, 0, M],
        [M, 15, 1, 0]
    ]

    testing3 = [
        [0, M, 3, M],
        [2, 0, M, M],
        [M, M, 0, M],
        [M, 1, 15, 0]
    ]

    tester = floyd_algorithm(testing)
    tester2 = floyd_algorithm(testing2)
    tester3 = floyd_algorithm(testing3)



