from itertools import combinations

n, m = map(int, input().split())
comb = [[True] * n for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    comb[x-1][y-1] = False
    comb[y-1][x-1] = False

result = 0
for i in combinations(range(n), 3):
    if comb[i[0]][i[1]] and comb[i[1]][i[2]] and comb[i[0]][i[2]]:
        result += 1

print(result)