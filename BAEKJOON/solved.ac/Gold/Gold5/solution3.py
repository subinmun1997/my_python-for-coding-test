from collections import deque
n, m = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(m)]

queue = deque()
for i in range(m):
    for j in range(n):
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

            if nx >= 0 and nx < m and ny >= 0 and ny < n and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append((nx, ny))

bfs()
res = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    res = max(res, max(i))

print(res-1)