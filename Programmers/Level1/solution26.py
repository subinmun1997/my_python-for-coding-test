import math

def solution(n, m):
    array = []
    array.append(math.gcd(n, m))
    array.append(math.lcm(n, m))
    return array

print(solution(3, 12))
print(solution(2, 5))