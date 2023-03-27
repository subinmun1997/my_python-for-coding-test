def solution(n, a, b):
    count = 0
    while a != b:
        a -= a//2
        b -= b//2
        count += 1

    return count

print(solution(8, 4, 7))