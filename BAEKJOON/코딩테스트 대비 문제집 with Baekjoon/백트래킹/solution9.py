from itertools import permutations

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

result = set(permutations(numbers, m))
for i in sorted(result):
    print(*i)