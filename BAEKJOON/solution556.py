from itertools import product

n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]
result = product(numbers, repeat=m)
for r in result:
    print(*r)