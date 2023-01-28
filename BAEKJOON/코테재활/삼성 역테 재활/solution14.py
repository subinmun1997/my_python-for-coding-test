from copy import deepcopy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def watch(x, y, direction, temp):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or temp[nx][ny] == 6:
                break
            elif temp[nx][ny] == 0:
                temp[nx][ny] = '#'

def dfs(n, graph):
    global answer
    temp = deepcopy(graph)

    if n == len(cctv):
        count = 0
        for t in temp:
            count += t.count(0)
        answer = min(answer, count)
        return

    x, y, c = cctv[n]
    for d in direction[c]:
        watch(x, y, d, temp)
        dfs(n+1, temp)
        temp = deepcopy(graph)

cctv = []
answer = 1e9

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and graph[i][j] != 6:
            cctv.append([i, j, graph[i][j]])

dfs(0, graph)
print(answer)