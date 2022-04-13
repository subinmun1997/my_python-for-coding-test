from itertools import combinations

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

result = set(combinations(numbers, m))
for i in sorted(result):
    print(*i)