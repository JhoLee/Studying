###
# Greedy Algorithm for FractionalKnapsack Problem
#
# Date: 17.11.18
#
# Author: 1626035, Jho
#
# +)
#    < 부분 배낭 문제를 위한 그리디 알고리즘 >
#   - 입력: n개의 물건과 각 물건의 무게와 가치, 베낭의 용량 C
#   - 출력: 베낭에 담은 물건 리스트 L과 베낭에 담은 물건의 가치 합 v
#   1) 각 물건의 단위 무게당 가치를 계산한다.
#   2) 물건들을 단위 무게당 가치를 기준으로 내림차순으로 정렬하고, 정렬된 물건 리스트를 S라 하자.
#   3) L = Null, w = 0, v = 0
#       // L은 배낭에 담을 물건 리스트,
#       // w는 배낭에 담긴 물건들의 무게의 합
#       // v는 배낭에 담긴 물건들의 가치의 합
#   4) S에서 단위 무게당 가치가 가장 큰 물건 x를 가져온다.
#   5) while ( ( w+x의 무게 <= C ) {
#   6)      x를 L에 추가시킨다.
#   7)      w = w + x의 무게
#   8)      v = v + x의 가치
#   9)      x를 S에서 제거한다.
#   10)     S에서 단위 무게당 가치가 가장 큰 물건 x를 가져온다.
#       }
#   11) if ( (C-w) > 0) {   // 배낭에 물건을 부분적으로 더 담을 여유가 있으면
#   12)     물건 x를 (C-w)만큼만 L에 추가한다.
#   13)     v = v +(C-w)만큼의 x의 가치
#       }
#   14) return L, v
#
#
###

## Data Settings ##
list = [
   # label, unit weight, value, price per unit weight #
    ['주석', 50, 50000, 0],
    ['백금', 10, 600000, 0],
    ['은', 25, 100000, 0],
    ['금', 15, 750000, 0]
]
C = 40      # Capacity of knapsack

n = len(list) # Number of items

L = [[], [], [], []]    # List of items in knapsack
w = 0       # Sum of the weight of the items in the knapsack
v = 0       # Sum of the value of the items in the knapsack
S = []    # Sorted list of items in knapsack
####

## Calculate the 'price per unit weight' of each item ##
for item in list:
    item[3] = item[2] / item[1]
####

## Sorts items in descending order by value per unit weight ##
# Used Selection Sort #
S = list
for i in range(0, n-1):
    for j in range(i+1, n):
        if S[i][3] < S[j][3]:
            S[i], S[j] = S[j], S[i]
##
####

# Putting in the knapsack #

i = 0   # indicator
if i < n:
    x = S[i]
else:
    x = []

## ##
while (x != [] and w + x[1]) <= C:
    L[i] = ([x[0], x[1]])
    w += x[1]
    v += x[2]

    # Deleting.. #
    x[0] = ""
    x[1] = 0
    x[2] = 0
    x[3] = 0.0

    i += 1
    if S != []:
        x = S[i]
    else:
        x = []
##

# #
if C-w > 0:
    L[i] = [x[0], C-w]
    x[1] -= C-w
    x[2] -= x[3] * (C-w)
    w += (C-w)
    v += x[3] * (C-w)
##

# Result Output #
i = 0
while L[i] != []:
    print("%s %dg" % (L[i][0], L[i][1]))
    i += 1
print("-----------")
print("배낭에 위와 같이 들어있으며,")
print("전체 가치는 %d원 입니다." % (v))
# #

## EOF ##
