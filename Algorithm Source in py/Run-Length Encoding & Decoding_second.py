##
# 17.11.22
#
# Run-Length Encoding & Decoding
#
# Author: Jho
#
# 주석 많이 제거, 과정 출력 버전
#
##

# Run-Length Encoding #
def RLE(subject):
    print("## 인코딩 시작..")
    print()
    result = ""

    n = len(subject)

    i = 0
    while i < n:

        count = 1
        j = i + 1

        ## ##
        while j < n and subject[i] == subject[j] and count < 9:
            count += 1
            j += 1
        ## End of Loop ##

        ## 3번 초과 반복된 경우에만 변환 ##
        if count > 3:
            print("변환 발생! ", end="")
            temp = "&" + str(count) + subject[i]
            result += temp
            print("%s -> %s" % (subject[i:j], temp))
        else:
            result += subject[i:j]
            print("%s -> %s" % (subject[i], subject[i]))
        ## ##
        print("결과 변수에 저장된 문자열: ", result)
        print()
        i = j
    ## ##
    print("인코딩 완료!!")
    print()
    return result
# #

# Run-Length Decoding #
def RLD(subject):
    print("## 디코딩 시작.. ")
    print()

    n = len(subject)
    result = ""     # 디코딩 값을 저장할 변수
    ## Loop ##
    i = 0
    while i < n:
        ### 변환된 부분 만남 ###
        if subject[i] == "&":
            count = int(subject[i+1])
            character = subject[i+2]

            temp = ""
            for j in range(0, count):
                temp += subject[i+2]

            result += temp
            i += 3

            print("%s -> %s " % (subject[i:i+3], temp))
        ### ###
        else:
            print("%s -> %s " % (subject[i], subject[i]))
            result += subject[i]
            i += 1
        print("결과 변수에 저장된 문자열: ", result)
        print()
    ## ##
    print("디코딩 완료!!")
    print()
    return result
# #

# main #
originData = "aaaaaefbbbbbbcdefg"
print("원본 문자열: " + originData)
print()

encodedData = RLE(originData)
print("  인코딩 후: " + encodedData)
print()

decodedData = RLD(encodedData)
print("  디코딩 후: " + decodedData)
print()

print("*********************************")
print("원본 문자열: " + originData)
print("  인코딩 후: " + encodedData)
print("  디코딩 후: " + decodedData)
print("*********************************")