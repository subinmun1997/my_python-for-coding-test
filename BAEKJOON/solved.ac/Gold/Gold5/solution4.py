from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif tomato[nx][ny] == 1:
                continue
            elif tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append((nx, ny))

bfs()
result = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    result = max(result, max(i))

print(result-1)
