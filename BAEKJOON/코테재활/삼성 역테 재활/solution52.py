def change_dir(d):
    # 오른쪽 or 위쪽 방향이었다면 왼쪽 or 아래쪽 방향으로
    if d in [0, 2]:
        d += 1
    # 왼쪽 or 아래쪽 방향이었다면 오른쪽 or 위쪽 방향으로
    elif d in [1, 3]:
        d -= 1
    return d

def solve(h_num):
    x, y, d = horse[h_num]
    nx = x + dx[d]
    ny = y + dy[d]

    # 범위를 벗어나거나 이동할 칸이 파란색이라면 방향 전환
    if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 2:
        d = change_dir(d)
        # 새로운 방향 저장
        horse[h_num][2] = d
        # 방향 전환하고 한 칸 이동
        nx = x + dx[d]
        ny = y + dy[d]
        # 그래도 범위를 벗어나거나 파란칸이라면 이동 멈춤
        if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 2:
            return True

    # 현재 말 부터 위로 쌓인 모든 말은 한번에 같이 이동
    horse_up = []
    for h_idx, h_n in enumerate(chess[x][y]):
        if h_n == h_num:
            horse_up.extend(chess[x][y][h_idx:])
            chess[x][y] = chess[x][y][:h_idx]
            break

    # 이동할 칸이 빨간색이라면 말 순서 전환
    if graph[nx][ny] == 1:
        horse_up = horse_up[::-1]

    for h in horse_up:
        # 해당 말의 위치 바꿔서 저장하기
        horse[h][0], horse[h][1] = nx, ny
        # 해당 칸에 말 추가
        chess[nx][ny].append(h)

    # 4개 이상의 말이 쌓였다면 게임 중단
    if len(chess[nx][ny]) >= 4:
        return False

    return True


# 입력 조건
n, k = map(int, input().split())
# 0=흰색, 1=빨간색, 2=파란색
graph = [list(map(int, input().split())) for _ in range(n)]
# 체스판 칸 위에 올려져 있는 말 번호 저장
chess = [[[] for _ in range(n)] for _ in range(n)]

# (말의 위치, 이동 방향) 저장
horse = []
for i in range(k):
    x, y, d = map(int, input().split())
    horse.append([x-1, y-1, d-1])
    chess[x-1][y-1].append(i)

dx = [0, 0, -1, 1] # 오, 왼, 위, 아래
dy = [1, -1, 0, 0]

# 출력 조건
count = 0
while True:
    flag = False

    # 턴이 1000보다 크면 -1 출력하고 종료
    if count > 1000:
        print(-1)
        break

    # 한 턴은 k개의 말을 다 이동시키는 것임
    for i in range(k):
        # solve함수가 false를 리턴하면(한 칸에 4개 이상의 말이 쌓이면) 게임 종료하기
        if not solve(i):
            flag = True
            break
    # k개의 말이 다 이동했으면 턴 하나 증가
    count += 1

    if flag:
        print(count)
        break
