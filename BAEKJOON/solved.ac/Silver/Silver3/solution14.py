from itertools import combinations

n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]

comb = combinations(numbers, m)
for i in comb:
    print(*i)