def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i

    return result

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(factorial(m) // (factorial(n) * factorial(m-n)))
