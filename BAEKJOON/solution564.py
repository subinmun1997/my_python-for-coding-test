# 중복순열

from itertools import product
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
result = set(product(numbers, repeat=m))
for r in sorted(result):
    print(*r)