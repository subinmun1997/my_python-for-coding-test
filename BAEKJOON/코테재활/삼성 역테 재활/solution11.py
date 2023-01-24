from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
members = [i for i in range(n)]

result = int(1e9)
for r1 in combinations(members, n//2):
    start, link = 0, 0
    r2 = list(set(members) - set(r1))

    for r in combinations(r1, 2):
        start += s[r[0]][r[1]]
        start += s[r[1]][r[0]]

    for r in combinations(r2, 2):
        link += s[r[0]][r[1]]
        link += s[r[1]][r[0]]

    result = min(result, abs(start - link))

print(result)