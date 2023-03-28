from collections import Counter

def solution(k, tangerine):
    cnt = Counter(tangerine)

    result = 0
    for v in sorted(cnt.values(), reverse=True):
        k -= v
        result += 1
        if k <= 0:
            break

    return result

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))