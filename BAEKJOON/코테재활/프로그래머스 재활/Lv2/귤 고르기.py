from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnt = Counter(tangerine)

    for i in sorted(cnt.values(), reverse=True):
        if k > 0:
            k -= i
            answer += 1
        else:
            break
    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))