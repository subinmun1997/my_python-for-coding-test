import math

def solution(n, m):
    return [math.gcd(n, m), math.lcm(n, m)]

print(solution(3, 12))
print(solution(2, 5))