# 방의 크기
n, m = map(int, input().split())
# (x, y): 로봇 청소기가 있는 칸의 좌표, direction: 바라보는 방향
# 0: 북쪽, 1: 동쪽, 2:남쪽, 3:서쪽
x, y, direction = map(int, input().split())
# 장소의 상태
# 0: 빈칸, 1: 벽
graph = [list(map(int, input().split())) for _ in range(n)]
# 청소 유무 0: 청소x, 1: 청소o
visited = [[0] * m for _ in range(n)]
# 현재 칸 청소
visited[x][y] = 1

dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

# 반시계 방향 90도 회전 함수
def turn_left():
    global direction

    direction -= 1
    if direction == -1:
        direction = 3

# 청소하는 칸의 개수
# 현재 위치 미리 청소했으니 1부터 시작
result = 1
# 회전한 횟수
turn_time = 0
while True:
    turn_left()

    nx = x + dx[direction]
    ny = y + dy[direction]
    # 빈 칸이고 아직 청소 안했다면
    if graph[nx][ny] == 0 and visited[nx][ny] == 0:
        # 청소하기
        visited[nx][ny] = 1
        result += 1
        # 해당 칸으로 전진
        x, y = nx, ny
        turn_time = 0
        continue
    # 벽이거나 이미 청소한 칸이라면
    else:
        turn_time += 1
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 후진할 수 있다면
        if graph[nx][ny] == 0:
            x, y = nx, ny
        # 벽이라 후진할 수 없다면 멈추기
        else:
            break
        turn_time = 0

print(result)