def solution(a, b, n):
    answer = 0

    while n >= a:
        cola = n // a
        n -= cola * a
        n += cola * b
        answer += cola * b

    return answer

print(solution(2, 1, 20))
print(solution(3, 1, 20))