from itertools import combinations

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
result = combinations(numbers, m)

for i in result:
    print(*i)