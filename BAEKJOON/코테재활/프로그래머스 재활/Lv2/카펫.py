def solution(brown, yellow):
    answer = []
    total = brown + yellow  # a * b = total
    for b in range(1, total + 1):
        a = total // b
        if (total / b) % a == 0:  # total / b = a
            if a >= b:  # a >= b
                if 2 * a + 2 * b == brown + 4:  # 2*a + 2*b = brown + 4
                    return [a, b]

    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))