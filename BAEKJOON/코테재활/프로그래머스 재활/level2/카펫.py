def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for b in range(1, total + 1):
        a = total // b
        if (total / b) % a == 0:
            if a >= b:
                if 2 * a + 2 * b == brown + 4:
                    return [a, b]

    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))