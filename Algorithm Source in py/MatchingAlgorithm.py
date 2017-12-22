###
# Matching Algorithm
#
# Date: 17.11.17
#
# Author: 1626035, Jho
#
# +)
#    < 문자열 매칭 (string pattern matching) >
#   - 문자열로 구성된 텍스트속에 주어진 패턴과 일치하는 부분이 있는지를 조사하는 문제로 문자열 탐색(string searching)이라 불리움
#   - 텍스트 에디터에서의 탐색이라는 명령과 텍스트 DB 에 있어서의 탐색등에서 조작으로 사용 됨
#   - 텍스트 상에서 찾으려는 문자열이 있는 열의 최초 의 위치를 구하거나 찾는 문자열이 없을 경우에는 찾으려는 문자열이 없다는 것을 표시
#   - 예. 찾으려는 pattern은 text에 position 9부터 존재함.
#      pattern     a b a b b
#      text        a b a b a a b b a b a b b a
#      position    1 2 3 4 5 6 7 8 9
#
# <간단한 매칭 알고리즘의 설명>
#   - 텍스트 상의 왼쪽 끝에 패턴을 두고 이들이 일치하는지를 조사
#   - 비교한 결과가 일치할 경우에는 텍스트의 처음 위치를 출력
#   - 일치하지 않을 경우에는 텍스트의 비교 위치를 우측으로 하나씩 이동하면서 일치하는 것이 나올 때까지 반복 작업을 실시
#
# Ver 1.0
###

## data set ##
pattern = "ababb"
text = "ababaabbababba"

position = -1       # Result position

n = len(text)       # length of 'text'
k = len(pattern)    # Length of Pattern

i = 0           # current 'Start pointer'


## Check ##
while(position < 0 and i + k <= n):
    count = 0
    temp = text[i:i + k]
    for j in range(0, k):
        if temp[j] != pattern[j]:
            break
        else:
            count += 1
    if(count == k):
        position = i + 1
    else:
        i += 1
################


print(position)

