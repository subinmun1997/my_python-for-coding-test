def solution(n):
    num = n ** 0.5
    return (num+1) ** 2 if num == int(num) else -1

print(solution(121))
print(solution(3))