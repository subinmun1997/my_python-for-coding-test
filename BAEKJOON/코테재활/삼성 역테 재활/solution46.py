from copy import deepcopy

def dust_in(x, y):
    temp = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
            temp += graph[nx][ny] // 5

    return temp

def dust_out(x, y):
    # 현재 칸으로부터 확산되어 나가는 미세먼지 양
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 내이고 공기청정기 위치가 아니라면
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
            cnt += 1

    return (graph[x][y] // 5) * cnt

def air_clean(graph, new_graph):
    # 공기청정기 윗 방향 (반시계 방향)
    graph[air-1][1] = 0
    for i in range(2, c):
        graph[air-1][i] = new_graph[air-1][i-1]

    for i in range(air-2, -1, -1):
        graph[i][-1] = new_graph[i+1][-1]

    for i in range(c-2, -1, -1):
        graph[0][i] = new_graph[0][i+1]

    for i in range(1, air-1):
        graph[i][0] = new_graph[i-1][0]

    for i in range(1, air-1):
        for j in range(1, c-1):
            graph[i][j] = new_graph[i][j]

    # 공기청정기 아래 방향 (시계 방향)
    graph[air][1] = 0
    for i in range(2, c):
        graph[air][i] = new_graph[air][i-1]

    for i in range(air+1, r):
        graph[i][-1] = new_graph[i-1][-1]

    for i in range(c-2, -1, -1):
        graph[r-1][i] = new_graph[r-1][i+1]

    for i in range(r-2, air, -1):
        graph[i][0] = new_graph[i+1][0]

    for i in range(air+1, r-1):
        for j in range(1, c-1):
            graph[i][j] = new_graph[i][j]

# 입력 조건
r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

# 상 하 좌 우 방향 선언
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 공기 청정기 위치 찾기
for i in range(r):
    if graph[i][0] == -1:
        air = i + 1
        break

# t초 동안 반복
for _ in range(t):
    new_graph = deepcopy(graph)
    for x in range(r):
        for y in range(c):
            # 공기청정기가 있는 위치가 아니라면
            if graph[x][y] != -1:
                # 총 미세먼지의 이동은 (해당 칸에 들어온 미세먼지 - 해당 칸으로 부터 확산된 미세먼지)
                total_dust = dust_in(x, y) - dust_out(x, y)
                # 현재 칸에서 발생한 미세먼지 이동 더해주기
                new_graph[x][y] += total_dust
    # 미세먼지 확산 끝나면 공기청정기 작동
    air_clean(graph, new_graph)

# 출력 조건
result = 0
for x in range(r):
    for y in range(c):
        # 공기 청정기 위치가 아니라면 미세먼지 양 더해주기
        if graph[x][y] != -1:
            result += graph[x][y]

print(result)

