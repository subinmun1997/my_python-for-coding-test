#중복조합

from itertools import combinations_with_replacement
n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
result = set(combinations_with_replacement(numbers, m))
for r in sorted(result):
    print(*r)