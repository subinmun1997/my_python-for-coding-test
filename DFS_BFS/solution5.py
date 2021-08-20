def factorial_iterative(n): # 반복적으로 구현한 n!
    result = 1
    for i in range(1, n+1):
        result *= i

    return result

print(factorial_iterative(5))