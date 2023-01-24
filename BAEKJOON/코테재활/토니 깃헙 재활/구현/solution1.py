import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

maxValue = 0

def dfs(x, y, dsum, cnt):
    global maxValue

    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, dsum + board[nx][ny], cnt+1)
            visited[nx][ny] = False

def exec(x, y):
    global maxValue
    for i in range(4):
        temp = board[x][y]
        for j in range(3):
            t = (i+j)%4
            nx = x + dx[t]
            ny = y + dy[t]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                temp = 0
                break
            temp += board[nx][ny]

        maxValue = max(maxValue, temp)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False

        exec(i, j)

print(maxValue)