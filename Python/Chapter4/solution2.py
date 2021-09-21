'''
입력값과 결괏값에 따른 함수의 형태
'''

# 일반적인 함수
# 입력값이 있고 결괏값이 있는 함수가 일반적인 함수이다.

def add(a, b):
    result = a + b
    return result

print(add(3,4))

# 입력값이 없는 함수
def say():
    return "Hi"

a = say()
print(a)

# 결괏값이 없는 함수
def add2(a, b):
    print("%d, %d의 합은 %d입니다." %(a,b,a+b))

add2(3,4)

# 입력값도 결괏값도 없는 함수
def say():
    print("Hi")

say()