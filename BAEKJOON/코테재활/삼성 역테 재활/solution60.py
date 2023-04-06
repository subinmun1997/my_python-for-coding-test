from copy import deepcopy

graph = [[] for _ in range(4)]

#     ↑,  ↖,  ←, ↙, ↓, ↘, →,  ↗
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        fish.append([data[2*j], data[2*j+1]-1])
    graph[i] = fish

max_score = 0
def dfs(sx, sy, score, graph):
    global max_score
    score += graph[sx][sy][0]
    max_score = max(max_score, score)
    graph[sx][sy][0] = 0

    # 물고기 움직임
    for f in range(1, 17):
        fx, fy = -1, -1
        for x in range(4):
            for y in range(4):
                if graph[x][y][0] == f:
                    # 해당 순번 물고기의 위치
                    fx, fy = x, y
                    break
        if fx == -1 and fy == -1:
            continue
        # 해당 순번 물고기의 방향
        fd = graph[fx][fy][1]

        for i in range(8):
            # 8방향 살펴보며 갈 수 있는 방향이 있는지 확인
            nd = (fd + i) % 8
            nx = fx + dx[nd]
            ny = fy + dy[nd]

            # 범위를 벗어나거나 해당 위치에 상어가 있다면
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            # 갈 수 있는 방향으로 방향 바꿈
            graph[fx][fy][1] = nd
            graph[fx][fy], graph[nx][ny] = graph[nx][ny], graph[fx][fy]
            break

    sd = graph[sx][sy][1]
    for i in range(1, 4):
        nx = sx + dx[sd] * i
        ny = sy + dy[sd] * i
        if (0 <= nx < 4 and 0 <= ny < 4) and graph[nx][ny][0] > 0:
            dfs(nx, ny, score, deepcopy(graph))

dfs(0, 0, 0, graph)
print(max_score)