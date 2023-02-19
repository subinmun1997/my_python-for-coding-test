n, m = map(int, input().split())
x, y, direction = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

d = [[0] * m for _ in range(n)]  # 로봇 청소기의 방문 여부 체크
d[x][y] = 1  # 로봇 청소기의 초기 위치 방문으로 변경

dx = [-1, 0, 1, 0]  # 북 동 남 서
dy = [0, 1, 0, -1]


def turn_left():
    global direction

    # 반시계 방향으로 회전 (북->서, 서->동, 동->남, 남->북)
    direction -= 1
    if direction == -1:  # 북 -> 서
        direction = 3


count = 1  # 초기 위치는 청소를 했으니 1로 초기화
turn_time = 0  # 로봇 청소기가 회전하는 수
while True:
    turn_left()  # 회전하며 청소되지 않은 빈 칸 여부를 파악
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:  # 빈 칸이며, 방문하지 않은 곳이라면
        d[nx][ny] = 1  # 방문 체크 해준다.
        count += 1  # 청소해야 되니까 count 수를 하나 증가
        x, y = nx, ny  # 해당 위치로 변경
        turn_time = 0  # 회전 카운트를 다시 0으로 초기화
        continue
    else:
        turn_time += 1  # 벽이거나 방문한 곳이라면 회전

    if turn_time == 4:  # 상 하 좌 우를 다 돌아봤다면
        nx = x - dx[direction]  # 바라보는 방향을 유지한 채로 한칸 후진
        ny = y - dy[direction]

        if array[nx][ny] == 0:  # 빈 칸이어서 후진이 가능하다면 위치 변경
            x, y = nx, ny
        else:  # 벽이라서 후진할 수 없다면 작동 멈춤
            break
        turn_time = 0

print(count)