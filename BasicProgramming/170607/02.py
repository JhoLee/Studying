##기초프로그래밍 최종 레포트01

a=int(input("첫번째 수를 입력하세요. 수 = "))

b=int(input("두번째 수를 입력하세요. 수 = "))

abs = a - b

if (abs<0):
    abs = abs * (-1)

print("입력된 두 수는 %d, %d 이며, 이 두 수의 절대값은 %d입니다." % (a, b, abs))