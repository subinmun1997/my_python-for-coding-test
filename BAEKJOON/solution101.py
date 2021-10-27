n, k = map(int, input().split())

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

value = factorial(n) // (factorial(k) * factorial(n-k))
print(value)

'''
이항 계수 : n! / (k!(n-k)!)
'''