from itertools import combinations

n = int(input())
member = [i for i in range(n)]
matrix = [list(map(int, input().split())) for _ in range(n)]

result = int(1e9)
for r1 in combinations(member, n//2):
    start, link = 0, 0
    r2 = list(set(member) - set(r1))

    for r in combinations(r1, 2):
        start += matrix[r[0]][r[1]]
        start += matrix[r[1]][r[0]]
    for r in combinations(r2, 2):
        link += matrix[r[0]][r[1]]
        link += matrix[r[1]][r[0]]
    result = min(result, abs(start-link))

print(result)