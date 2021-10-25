data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

'''
일반적으로 특정한 두 수에 대하여 연산을 수행할 때, 대부분은 '+' 보다는 'x' 가 더 값을 크게 만든다.
하지만 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기를 수행하는 것이 효율적이다.
즉, 두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 더하며, 두 수가 모두
2 이상인 경우에는 곱하면 된다.
'''