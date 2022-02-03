def oper(a, b):
    total = 1
    for i in range(a, b+1):
        plus = 0
        for j in range(1, i+1):
            plus += j
        total *= plus
    return total

a, b = map(int, input().split())
result = oper(a, b)
print(result % 14579)