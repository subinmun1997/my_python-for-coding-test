n = int(input())

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i

    return result

num = str(factorial(n))[::-1]

count = 0
for i in num:
    if i == '0':
        count += 1
    else:
        break

print(count)

