from collections import deque

def biteFish(x, y, size):
    # 방문여부 체크
    visited = [[0 for _ in range(n)] for _ in range(n)]
    # 아기상어와 물고기 사이의 거리 기록
    distance = [[0 for _ in range(n)] for _ in range(n)]

    queue = deque()
    queue.append((x, y))
    # 현 위치 방문처리
    visited[x][y] = 1
    possibleEat = [] # 먹을 수 있는 물고기 위치 저장 배열

    while queue:
        cur_x, cur_y = queue.popleft()
        # 네 방향을 살펴보며
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            # 범위 내이고, 방문한 적이 없다면
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 상어는 자신의 크기보다 작거나 같은 물고기가 있는 칸만 지나갈 수 있다
                if graph[nx][ny] <= size:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    # 거리는 직전 위치보다 하나 늘려주고 저장
                    distance[nx][ny] = distance[cur_x][cur_y] + 1
                    # 상어의 크기보다 작고 and 빈 칸이 아니라면 -> 먹을 수 있는 물고기
                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        # 위치와 거리 저장
                        possibleEat.append((nx, ny, distance[nx][ny]))

    # 1.거리가 가까운 물고기 2. 가장 위에 있는 물고기 3. 가장 왼쪽에 있는 물고기
    # pop()해서 사용할 것이기 때문에 내림차순으로 정렬
    return sorted(possibleEat, key=lambda x : (-x[2], -x[0], -x[1]))

# 입력 조건
n = int(input())
# 0=빈칸, 9=아기상어, 1~6:물고기 크기
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y, size = 0, 0, 2
for i in range(n):
    for j in range(n):
        # 해당 칸에 아기 상어가 있다면 x, y값에 위치 저장해주기
        if graph[i][j] == 9:
            x, y = i, j

cnt = 0 # 먹은 물고기의 수
result = 0 # 아기 상어가 혼자 물고기를 잡아먹을 수 있는 초
while True:
    shark = biteFish(x, y, size)

    # 먹을 수 있는 물고기가 없다면 끝내기
    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()
    # 물고기 먹으러 가기위한 거리 더해주기
    result += dist
    # 아기상어의 위치 0으로 바꿈
    graph[x][y] = 0
    # 물고기를 먹으면 해당 칸은 빈 칸이 된다
    graph[nx][ny] = 0
    x, y = nx, ny

    # 먹은 물고기 수 증가
    cnt += 1
    # 아기 상어의 크기와 먹은 물고기 수가 같다면 크기가 1증가
    if cnt == size:
        size += 1
        cnt = 0

print(result)