from itertools import permutations

n, m = map(int, input().split())
number = [i for i in range(1, n+1)]

perm = permutations(number, m)
for i in perm:
    print(*i)