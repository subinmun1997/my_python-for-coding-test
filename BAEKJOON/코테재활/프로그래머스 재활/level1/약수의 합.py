def solution(n):
    return sum([i for i in range(1, n+1) if n % i == 0])

print(solution(12))
print(solution(5))