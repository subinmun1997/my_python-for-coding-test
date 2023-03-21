# 입력 조건
n, m = map(int, input().split())
# (x, y) = 로봇 청소기가 있는 칸의 좌표, direction = 로봇 청소기가 바라보는 방향
x, y, direction = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

d = [[0] * m for _ in range(n)] # 방문 체크 배열
d[x][y] = 1 # 현재 로봇 청소기의 위치 방문 체크

dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

# 반시계 방향으로 90도 회전 함수 구현
def turn_left():
    # 현재 로봇청소기의 방향
    global direction
    # 반시계 방향이니까 -1 해주기
    direction -= 1
    # 북 -> 서로 이동하는 경우는 따로 체크
    if direction == -1:
        direction = 3

count = 1 # 로봇 청소기가 청소하는 총 칸의 개수(초기 위치는 바로 청소 시작하므로 1로 초기화)
turn_time = 0 # 반시계 방향으로 회전하는 횟수
while True:
    turn_left() # 위에서 초기화 위치 청소 했으니 바로 회전부터 시작
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 방문하지 않는 곳이고(청소 안되어있음), 해당 위치가 벽이 아니라면
    if d[nx][ny] == 0 and graph[nx][ny] == 0:
        d[nx][ny] = 1 # 방문 처리
        count += 1 # 청소한 칸 개수 하나 증가
        x, y = nx, ny # 로봇 청소기의 위치 이동
        turn_time = 0 # 회전하는 횟수는 다시 0으로 초기화
        continue
    # 방문했거나 또는 해당 위치가 벽이라 이동할 수 없다면
    else:
        turn_time += 1
    # 현재 칸의 주변 4칸 모두 청소되지 않은 빈 칸이 없는 경우
    if turn_time == 4:
        # 바라보는 방향을 유지한 채로 한 칸 후진해보기
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 후진 할 수 있다면
        if graph[nx][ny] == 0:
            x, y = nx, ny
        # 후진 할 수 없다면 끝내기
        else:
            break
        # 후진 했다면 다시 회전하는 횟수를 0으로 초기화
        turn_time = 0

print(count)