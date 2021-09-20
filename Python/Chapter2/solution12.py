# 불 자료형
a = True
b = False
print(a,b)

print(type(a))
print(type(b))

# 조건문의 반환 값
print(1==1)
print(2>1)
print(2<1)

# 자료형의 참과 거짓
a = [1,2,3,4]
while a:
    print(a.pop())

if []:
    print("참")
else:
    print("거짓")

if [1,2,3]:
    print("참")
else:
    print("거짓")

# 불 연산
print(bool('python'))
print(bool(''))
print(bool([1,2,3]))
print(bool([]))
print(bool(0))
print(bool(3))