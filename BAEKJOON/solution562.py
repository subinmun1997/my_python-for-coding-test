# 순열_set 사용

from itertools import permutations
n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

result = set(permutations(numbers, m))
for r in sorted(result):
    print(*r)