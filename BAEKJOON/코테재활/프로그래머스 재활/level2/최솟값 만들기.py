def solution(a, b):
    return sum([x * y for x, y in zip(sorted(a), sorted(b, reverse=True))])

print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1,2], [3,4]))