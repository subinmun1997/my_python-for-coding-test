def dfs(x, y):
    global cnt
    # 범위를 벗어나면 false
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

# 지도의 크기
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 총 단지 수
village = 0
# 각 단지내 집의 수
home = []
cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            village += 1
            dfs(i, j)
            home.append(cnt)
            cnt = 0

print(village)
for h in sorted(home):
    print(h)