'''
백준 15686 치킨 배달 - dfs 풀이
'''
def distance(select_chicken):
    dist = 0
    for h in house:
        dist += min(abs(h[0] - i[0]) + abs(h[1] - i[1]) for i in select_chicken)
    return dist

def dfs(depth, idx):
    global result

    if depth == m:
        select_chicken = [chicken[i] for i in range(len(chicken)) if used[i]]
        result = min(result, distance(select_chicken))
        return

    for i in range(idx, len(chicken)):
        if used[i] == False:
            used[i] = True
            dfs(depth+1, i+1)
            used[i] = False


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        if graph[i][j] == 2:
            chicken.append((i, j))

result = int(1e9)
used = [False] * len(chicken)
dfs(0, 0)

print(result)