from collections import deque

n, k = map(int, input().split())
graph = []
virus = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j))

virus.sort()
queue = deque(virus)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while queue:
    virus, s, x, y = queue.popleft()

    if target_s == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < n:

            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])