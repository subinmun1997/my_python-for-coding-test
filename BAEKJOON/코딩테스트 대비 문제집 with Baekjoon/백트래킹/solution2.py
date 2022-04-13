from itertools import combinations

n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]
result = combinations(numbers, m)

for i in result:
    print(*i)