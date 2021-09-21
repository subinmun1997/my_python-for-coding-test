# 여러 개의 입력값을 받는 함수 만들기

def add_many(*args): # 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아서 튜플로 만들어 준다.
    result = 0
    for i in args:
        result += i
    return result

result1 = add_many(1,2,3)
print(result1)

result2 = add_many(1,2,3,4,5,6,7,8,9,10)
print(result2)

# 예시 2
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i

    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result3 = add_mul('add', 1,2,3,4,5)
print(result3)

result4 = add_mul('mul', 1,2,3,4,5)
print(result4)

