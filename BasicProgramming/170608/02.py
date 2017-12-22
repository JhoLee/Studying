##기초프로그래밍 최종 레포트05

num = 1
odd_count = 0
odd_sum = 0
even_count = 0
even_sum = 0

while(num > 0):   print("마지막 숫자는 0을 입력합니다")
    num = int(input("홀수와 짝수를 판별하기위한 수를 입력하세요. 숫자는 ? = "))
    
    #홀짝 판별문
    if(num > 0):
        if(num  % 2 == 0):
            #짝수
            even_count += 1
            even_sum += num
        if(num % 2 == 1):
            #홀수
            odd_count += 1
            odd_sum += num
#반복문 종료

#결과 출력
print("입력된 홀수의 갯수는 %d개이며, 누적합은 %d 입니다." % (odd_count, odd_sum))
print("입력된 짝수의 갯수는 %d개이며, 누적합은 %d 입니다." % (even_count, even_sum))
    
