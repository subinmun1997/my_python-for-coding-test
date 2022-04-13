from itertools import product

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
result = set(product(numbers, repeat=m))

for i in sorted(result):
    print(*i)