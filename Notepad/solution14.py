n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())

d[x][y] = 1
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and graph[nx][ny] == 0:
        d[nx][ny] = 1
        count += 1
        turn_time = 0
        x = nx
        y = ny
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if graph[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)