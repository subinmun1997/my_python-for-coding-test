def solution(n):
    return bin(n).count('1')

print(solution(5))
print(solution(6))
print(solution(5000))