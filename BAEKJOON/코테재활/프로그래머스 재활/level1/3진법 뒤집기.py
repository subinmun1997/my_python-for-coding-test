def three(n):
    answer = ''
    while n:
        answer += str(n%3)
        n //= 3
    return answer

def solution(n):
    n = three(n)
    return int(n, 3)

print(solution(45))
print(solution(125))

