from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

result = int(1e9)
for c in combinations(chicken, m):
    distance = 0
    for h in house:
        distance += min(abs(h[0] - i[0]) + abs(h[1] - i[1]) for i in c)
    result = min(result, distance)

print(result)
