# 매개변수 지정하여 호출하기

def add(a, b):
    return a+b

result = add(a=3, b=7)
print(result)

# 매개변수를 지정하면 다음과 같이 순서에 상관없이 사용할 수 있다는 장점이 있다.
result = add(b=5, a=3)
print(result)