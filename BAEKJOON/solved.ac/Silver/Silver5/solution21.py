t = int(input())

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

for _ in range(t):
    n, m = map(int, input().split())
    print(factorial(m) // (factorial(n) * factorial(m-n)))
