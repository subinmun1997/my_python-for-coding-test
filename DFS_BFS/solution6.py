def factorial_recursive(n): # 재귀적으로 구현한 n!

    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_recursive(5))