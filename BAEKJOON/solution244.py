n, k = map(int, input().split())
# 이항 계수 : n! / k! * (n-k)!

def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x-1)

value = factorial(n) // (factorial(k) * factorial(n-k))
print(value%10007)