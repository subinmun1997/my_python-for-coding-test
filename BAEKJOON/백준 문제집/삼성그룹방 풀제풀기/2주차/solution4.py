from collections import deque

def bfs(x, y):
    global cnt

    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt += 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내이고 집이 있다면
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                queue.append((nx, ny))

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
            bfs(i, j)
            home.append(cnt)
            cnt = 0

print(village)
for h in sorted(home):
    print(h)