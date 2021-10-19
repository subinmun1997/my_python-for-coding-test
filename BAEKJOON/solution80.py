def factorial(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num

for _ in range(int(input())):
    n, m = map(int, input().split())
    k = m - n
    print(int(factorial(m)/(factorial(k)*factorial(n))))
