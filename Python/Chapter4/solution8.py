# 함수 안에서 선언한 변수의 효력 범위

a = 1
def vartest(a): # 함수 안에서 새로 만든 매개변수는 함수 안에서만 사용하는 '함수만의 변수'이다.
    a = a + 1
    # 함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과는 전혀 상관이 없다.
vartest(a)
print(a)

# 함수 안에서 함수 밖의 변수를 변경하는 방법

# 1. return 사용하기
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

# 2. global 명령어 사용하기
b = 1
def vartest():
    global b # 함수 안에서 함수 밖의 b 변수를 직접 사용하겠다는 뜻
    b = b + 1
    '''
    프로그래밍을 할 때 global 명령어는 사용하지 않는 것이 좋다. 왜냐하면 함수는 독립적으로 존재하는 것이
    좋기 때문이다. 외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다.
    '''
vartest()
print(b)