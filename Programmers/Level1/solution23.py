def solution(n):
    check = n ** 0.5
    return (check+1) ** 2 if check == int(check) else -1

print(solution(121))
print(solution(3))
