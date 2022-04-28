def solution(n):
    check = int(n ** 0.5)
    if check ** 2 == n:
        return (check+1) ** 2
    else:
        return -1

print(solution(121))
print(solution(3))