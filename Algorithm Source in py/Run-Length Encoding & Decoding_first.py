##
# 17.11.22
#
# Run-Length Encoding & Decoding
#
# Author: Jho
#
##

# Run-Length Encoding #
def RLE(subject):
    result = "" # 인코딩 결과값을 저장할 변수

    n = len(subject)

    ## Loop ##
    i = 0
    while i < n:
        count = 1
        j = i + 1
        ## 루프 시작 ##
        ### 조건
        ### 1) i번 방의 문자와 j번 방의 문자가 같음 ###
        ### 2) 반복 횟수 10번 미만                  ###
        while j < n and subject[i] == subject[j] and count < 9:
            count += 1
            j += 1

        ## End of Loop ##

        ## 3번 초과 반복된 경우에만 변환 ##
        if count > 3:
            temp = "&" + str(count) + subject[i]
            result += temp
        else:
            result += subject[i:j]
        ## ##
        i = j
    ## ##
    return result
# #

# Run-Length Decoding #
def RLD(subject):
    n = len(subject)
    result = ""     # 디코딩 값을 저장할 변수
    ## Loop ##
    i = 0
    while i < n:
        ### 변환된 부분 만남 ###
        if subject[i] == "&":
            count = int(subject[i+1])
            character = subject[i+2]
            for j in range(0, count):
                result += subject[i+2]
            i += 3
        ### ###
        else:
            result += subject[i]
            i += 1
    ## ##
    return result
# #


if __name__ == "__main__":
    originData = "aaaaaefbbbbbbcdefg"
    encodedData = RLE(originData)
    decodedData = RLD(encodedData)

    print("원본 문자열: " + originData)
    print("  인코딩 후: " + encodedData)
    print("  디코딩 후: " + decodedData)