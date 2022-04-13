from itertools import combinations_with_replacement

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
result = combinations_with_replacement(numbers, m)

for i in result:
    print(*i)
