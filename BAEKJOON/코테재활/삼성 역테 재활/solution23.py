def move():
    #이동한 상어 위치 저장할 새로운 배열
    new_graph = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 0:
                x, y, s, d, z = i, j, graph[i][j][0], graph[i][j][1], graph[i][j][2]
                # 속력이 양수일 경우
                while s > 0:
                    x += dx[d]
                    y += dy[d]
                    if 0 <= x < R and 0 <= y < C:
                        # 범위 안이라면 속력 - 1
                        s -= 1
                    else:
                        x -= dx[d]
                        y -= dy[d]
                        # 범위를 벗어났다면 이전 칸으로 이동시키고 방향 전환
                        if d == 1: d = 2
                        elif d == 2: d = 1
                        elif d == 3: d = 4
                        elif d == 4: d = 3
                # 한번도 저장된 적 없는 위치라면 새롭게 저장
                if new_graph[x][y] == 0:
                    new_graph[x][y] = [graph[i][j][0], d, z]
                else:
                    # 아니라면 제일 큰 값 저장하기 위한 로직
                    if new_graph[x][y][2] < z:
                        new_graph[x][y] = [graph[i][j][0], d, z]
    return new_graph

dx = [0, -1, 1, 0, 0] # null 위 아래 오른쪽 왼쪽
dy = [0, 0, 0, 1, -1]

R, C, m = map(int, input().split())
graph = [[0 for _ in range(C)] for _ in range(R)]

for _ in range(m):
    r, c, s, d, z = map(int, input().split())
    # r,c에 [속도, 방향, 크기] 저장
    graph[r-1][c-1] = [s, d, z]

result = 0
for j in range(C):
    for i in range(R):
        if graph[i][j] != 0:
            # 0이 아니라면 result에 크기 더하고 해당 위치 0으로 바꾸기
            result += graph[i][j][2]
            graph[i][j] = 0
            break
    # 상어 이동
    graph = move()

print(result)