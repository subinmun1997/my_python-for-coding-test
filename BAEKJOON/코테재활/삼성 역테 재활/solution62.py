from copy import deepcopy

# 입력 조건
graph = [[] for _ in range(4)]
     # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # (물고기의 번호, 바라보는 방향) 저장
        # 방향 인덱스는 0부터 시작하므로 -1 하고 저장
        fish.append([data[2*j], data[2*j+1]-1])
    graph[i] = fish

# 출력 조건
# 상어가 먹을 수 있는 물고기 번호의 최대 합
max_score = 0
def dfs(sx, sy, score, graph): # 상어의 위치:(sx, sy)
    global max_score
    # 현재 상어가 위치한 곳의 물고기 번호 더해주기
    score += graph[sx][sy][0]
    # 최대 합 갱신
    max_score = max(max_score, score)
    # 상어가 먹은 물고기의 번호는 0으로 설정
    graph[sx][sy][0] = 0

    # 물고기의 이동
    for f in range(1, 17):
        fx, fy = -1, -1
        for x in range(4):
            for y in range(4):
                # f번째 물고기가 해당 위치에 있다면
                if graph[x][y][0] == f:
                    # 주소 갱신해주기
                    fx, fy = x, y
                    break
        # 만약 상어가 이미 먹어서 없는 물고기라면
        if fx == -1 and fy == -1:
            continue
        # 해당 물고기가 바라보고 있는 방향
        fd = graph[fx][fy][1]

        for i in range(8):
            # 8방향 하나씩 살펴보며 이동할 수 있는 곳인지 체크
            nd = (fd + i) % 8
            nx = fx + dx[nd]
            ny = fy + dy[nd]

            # 범위를 벗어나거나 이동할 위치에 상어가 있다면
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            # 물고기의 새로운 이동 방향 갱신
            graph[fx][fy][1] = nd
            # 위치 바꿔주기
            graph[fx][fy], graph[nx][ny] = graph[nx][ny], graph[fx][fy]
            break

    # 상어가 바라보는 방향
    sd = graph[sx][sy][1]
    # 상어가 이동할 수 있는 칸은 최대 3칸까지
    for i in range(1, 4):
        nx = sx + dx[sd] * i
        ny = sy + dy[sd] * i
        # 범위 내이고 해당 위치에 물고기가 있다면
        if (0 <= nx < 4 and 0 <= ny < 4) and graph[nx][ny][0] > 0:
            dfs(nx, ny, score, deepcopy(graph))

dfs(0, 0, 0, graph)
print(max_score)