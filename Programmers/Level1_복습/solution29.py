def solution(n):
    temp = ''
    while n:
        temp += str(n%3)
        n //= 3
    answer = int(temp, 3)

    return answer

print(solution(45))
print(solution(125))