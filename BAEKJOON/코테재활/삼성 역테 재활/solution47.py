def move():
    # 상어가 이동하고 나서, 새로운 상어의 위치를 저장해줘야 함
    new_graph = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            # 해당 위치에 상어가 있으면
            if graph[i][j] != 0:
                x, y, s, d, z = i, j, graph[i][j][0], graph[i][j][1], graph[i][j][2]
                # 속력이 양수인 동안 계속 상어 이동
                while s > 0:
                    # 상어의 방향대로 이동
                    x += dx[d]
                    y += dy[d]

                    # 이동한 방향이 범위 내이면, 속도 하나 감소
                    if 0 <= x < R and 0 <= y < C:
                        s -= 1
                    # 범위를 벗어났다면 한 칸 전으로 되돌리고, 방향을 바꿔줌
                    else:
                        x -= dx[d]
                        y -= dy[d]
                        if d == 1: d = 2
                        elif d == 2: d = 1
                        elif d == 3: d = 4
                        elif d == 4: d = 3

                # 상어가 이동한 방향에 다른 상어가 없다면
                if new_graph[x][y] == 0:
                    # 바로 저장
                    new_graph[x][y] = [graph[i][j][0], d, z]
                else: # 다른 상어가 있다면 제일 큰 상어 저장하기
                    if new_graph[x][y][2] < z:
                        new_graph[x][y] = [graph[i][j][0], d, z]

    return new_graph

# 입력 조건
R, C, M = map(int, input().split())
graph = [[0 for _ in range(C)] for _ in range(R)]

for _ in range(M):
    # (r, c)=상어의 위치, s=속력, d=이동 방향, z=크기
    r, c, s, d, z = map(int, input().split())
    graph[r-1][c-1] = [s, d, z]

dx = [0, -1, 1, 0, 0] # null, 위, 아래, 오른쪽, 왼쪽
dy = [0, 0, 0, 1, -1]

# 출력 조건
result = 0
for j in range(C):
    for i in range(R):
        # 해당 위치에 상어가 있으면
        if graph[i][j] != 0:
            # 상어의 크기만큼 더해줌 (한 번에 한 마리의 상어만 잡아야 되기 때문에 바로 break)
            result += graph[i][j][2]
            # 해당 위치는 0으로 바꿈
            graph[i][j] = 0
            break
    # 상어 이동
    graph = move()

print(result)