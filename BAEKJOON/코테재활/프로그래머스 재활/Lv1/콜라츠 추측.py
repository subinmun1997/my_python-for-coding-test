def solution(n):
    count = 0
    while n != 1:
        if count == 500:
            return -1
        if n%2:
            n = n * 3 + 1
        else:
            n //= 2
        count += 1
    return count

print(solution(6))
print(solution(16))
print(solution(626331))