from collections import deque

# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y, shark_size = 0, 0, 2
# 상어 위치
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j

def biteFish(x, y, size):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    distance = [[0 for _ in range(n)] for _ in range(n)]
    # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야 하는 칸의 개수의 최솟값이다. (bfs사용)

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    possibleEat = []

    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] <= size:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cur_x][cur_y] + 1
                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        possibleEat.append((nx, ny, distance[nx][ny]))
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기
    return sorted(possibleEat, key=lambda x : (-x[2], -x[0], -x[1]));

cnt = 0
result = 0
while True:
    shark = biteFish(x, y, shark_size)
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움 요청
    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()
    # 움직이는 칸 수가 곧 시간
    result += dist
    graph[nx][ny] = 0
    graph[x][y] = 0
    # 상어 좌표를 먹은 물고기 좌표로 옮겨준다.
    x, y = nx, ny
    cnt += 1

    if cnt == shark_size:
        shark_size += 1
        cnt = 0

print(result)