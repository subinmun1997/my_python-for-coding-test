from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

x, y, size = 0, 0, 2
# 아기 상어의 위치 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j

dx = [-1, 0, 1, 0] # 상 하 좌 우로 움직이기 위한 방향 설정
dy = [0, 1, 0, -1]

def biteFish(x, y, shark_size):
    visited = [[0 for _ in range(n)] for _ in range(n)] # 방문 여부
    distance = [[0 for _ in range(n)] for _ in range(n)] # 최소 거리

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1 # 아기 상어의 위치 방문 처리
    possibleEat = [] # 아기 상어가 먹을 수 있는 물고기 위치

    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            # 범위 안이고 방문한 적이 없다면
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 아기 상어보다 같거나 작다면 이동 가능
                if graph[nx][ny] <= shark_size:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cur_x][cur_y] + 1
                    # 아기 상어보다 크기가 작고, 물고기가 위치한 곳이라면 (빈 칸이 아니라면)
                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                        # 먹을 수 있는 물고기 위치로 저장
                        possibleEat.append((nx, ny, distance[nx][ny]))

    # 역순으로 정렬하는 이유: 리턴 받은 값을 popleft()가 아닌, pop()으로 출력하기 때문에 역순으로 정렬해서 반환해야 됨
    return sorted(possibleEat, key=lambda x : (-x[2], -x[0], -x[1]))

cnt = 0
result = 0 # 아기 상어 혼자 물고기를 잡아먹을 수 있는 총 시간(초)
while True:
    shark = biteFish(x, y, size)

    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()
    result += dist # 걸린 시간만큼 결과값에 더해주고
    graph[x][y] = 0 # 아기상어의 전의 위치 0으로 저장
    graph[nx][ny] = 0 # 먹은 물고기 위치 0으로 저장
    x, y = nx, ny

    cnt += 1
    if cnt == size: # 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
        size += 1
        cnt = 0

print(result)