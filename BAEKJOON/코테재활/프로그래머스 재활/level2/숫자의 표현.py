def solution(n):
    count = 0
    for i in range(1, n+1):
        temp = 0
        for j in range(i, n+1):
            temp += j
            if temp == n:
                count += 1
            elif temp > n:
                break

    return count

print(solution(15))