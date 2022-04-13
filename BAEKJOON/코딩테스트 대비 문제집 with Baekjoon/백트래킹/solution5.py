from itertools import permutations

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

result = permutations(numbers, m)
for i in result:
    print(*i)
