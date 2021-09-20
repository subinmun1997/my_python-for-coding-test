from copy import copy
# 자료형의 값을 저장하는 공간, 변수

# 변수가 가리키는 메모리의 주소
a = [1,2,3]
print(id(a)) # id 함수는 변수가 가리키고 있는 객체의 주소 값을 돌려주는 파이썬 내장 함수이다.

# 리스트를 복사할 때
a = [1,2,3]
b=a # b와 a는 완전히 동일
print(b)

print(id(a))
print(id(b))
print(a is b)

a[1] = 4
print(a)
print(b)

# b 변수를 생성할 때 a 변수의 값을 가져오면서 a와는 다른 주소를 가리키도록 만드는 방법
# [:] 사용
a = [1,2,3]
b = a[:]
print(a)
print(b)

a[1] = 4
print(a)
print(b)

# copy 모듈 사용
a = [1,2,3]
b = copy(a)
print(b)

print(a)
print(b)
print(b is a)

# 변수를 만드는 여러 가지 방법
a, b = ('python','life')
print(a,b)

(a,b) = 'python','life'
print(a,b)

[a,b] = ['python','life']
print(a,b)

a=b='python'
print(a,b)

a=3
b=5
print(a,b)
a,b = b,a
print(a,b)