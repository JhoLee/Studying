## 두 수 입력
a = int(input("a >> "))
b = int(input("b >> "))

##original
_a = a
_b = b

##
while(_a>=_b):
    if(_a>_b):
        _a -= _b
    else:
        temp = _a
        _a = _b
        _b = temp

## Print
print("두 수 %d, %d 의 최대공약수는 %d" % (a, b, _a))
