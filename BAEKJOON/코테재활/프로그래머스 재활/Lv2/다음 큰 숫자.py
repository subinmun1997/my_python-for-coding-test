def solution(n):
    n_count = bin(n)[2:].count('1')
    num = n+1

    while True:
        temp = bin(num)[2:].count('1')
        if temp == n_count:
            answer = num
            break
        else:
            num += 1

    return answer

print(solution(78))
print(solution(15))