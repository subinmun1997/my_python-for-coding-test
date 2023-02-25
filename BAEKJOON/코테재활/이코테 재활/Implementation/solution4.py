n, m = map(int, input().split())
x, y, direction = map(int, input().split())
visited = [[0] * m for _ in range(n)] # 방문 여부 체크
visited[x][y] = 1 # 현재 좌표 방문 처리

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction

    direction -= 1
    if direction == -1:
        direction = 3

turn_time = 0
count = 1
while True:
    turn_left()

    nx = x + dx[direction]
    ny = y + dy[direction]

    if graph[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        count += 1
        turn_time = 0
        x, y = nx, ny
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if graph[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(count)