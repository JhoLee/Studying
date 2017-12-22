##
#
# AllPairsShortest Algorithm
#
# Date: 17.11.29
#
# Author: Jho
#
##

# Data Set #
M = 88  # Max Value
D = [
    ['D', 1, 2, 3, 4, 5],
    [1, 0, 4, 2, 5, M],
    [2, M, 0, 1, M, 4],
    [3, 1, 3, 0, 1, 2],
    [4, -2, M, M, 0, 2],
    [5, M, -3, 3, 1, 0]
]
n = len(D)
# #

# Process #
for k in range(1, n):
    for i in range(1, n):
        if i is not k:
            for j in range(1, n):
                if (j is not k) and (j is not i):
                    D[i][j] = min(D[i][k] + D[k][j], D[i][j])
# #

# Output #
for i in range(0, n):
    for j in range(0, n):
        if i is 0 and j is 0:
            print("%3c" % D[i][j], end="")
        else:
            print("%3d" % D[i][j], end="")
    print()
print()
# #