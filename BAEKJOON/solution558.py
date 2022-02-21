# 순열

from itertools import permutations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
result = sorted(permutations(numbers, m))
for r in result:
    print(*r)
