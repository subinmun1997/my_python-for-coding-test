# 함수의 결괏값은 언제나 하나이다.
def add_and_mul(a,b):
    return a+b, a*b # 2개의 매개변수를 받아 더한 값과 곱한 값을 돌려준다.

result = add_and_mul(3,4) # add_and_mul 함수의 결괏값 a+b와 a*b는 튜플값 하나인 (a+b, a*b)로 돌려준다.
print(result)

result1, result2 = add_and_mul(3,4)
print(result1, result2)

def add_and_mul2(a,b):
    return a+b
    return a*b # 이 return문은 실행되지 않음

# 함수는 return문을 만나는 순간 결괏값을 돌려준 다음 함수를 빠져나가게 된다.

result3 = add_and_mul2(3,4)
print(result3)

# return의 또 다른 쓰임새
# 특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." %nick)

say_nick("야호")
say_nick("바보")