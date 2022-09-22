def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = int(input())
fact = str(factorial(n))[::-1]

count = 0
for i in fact:
    if i == '0':
        count += 1
    else:
        break

print(count)

