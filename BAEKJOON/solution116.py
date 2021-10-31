from itertools import combinations

INF = int(1e9)
n, m = map(int, input().split())


array = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for r in range(n):
    for c in range(n):
        if array[r][c] == 1:
            house.append((r,c))
        elif array[r][c] == 2:
            chicken.append((r,c))

result = INF
for c in combinations(chicken, m):
    distance = 0
    for h in house:
        distance += min([abs(h[0]-i[0]) + abs(h[1]-i[1]) for i in c])
    result = min(result, distance)

print(result)
