from collections import deque

# n * m 크기의 미로
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내이고, 이동할 수 있는 칸이라면
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                # 이전 칸보다 1칸 더 가면 된다
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0))