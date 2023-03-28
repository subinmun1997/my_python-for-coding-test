def solution(a, b, n):
    total = 0
    while n >= a:
        cola = n // a * b
        n = n % a + cola
        total += cola
    return total

print(solution(2, 1, 20))
print(solution(3, 1, 20))