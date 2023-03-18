# 정중앙으로부터 끝까지 움직이는 경로를 계산
def initialize_tragger_path():
    dx = [-1, 0, 1, 0] # 순방향일때 술래의 이동은 상 우 하 좌 순서
    dy = [0, 1, 0, -1]

    curr_x, curr_y = n // 2, n // 2 # 술래의 처음 시작 위치
    move_dir, move_num = 0, 1 # 술래의 처음 방향(위쪽으로 먼저 이동하므로 0), (1,1,2,2,3,3...)순서로 이동하니까 처음엔 1칸으로 설정

    while curr_x and curr_y: # (x,y)가 (0,0)이면 종료 -> 한바퀴 턴 끝난 것임
        # move_num 만큼 이동
        for _ in range(move_num):
            tragger_dir[curr_x][curr_y] = move_dir
            curr_x, curr_y = curr_x + dx[move_dir], curr_y + dy[move_dir] # 그 다음 이동 방향
            if move_dir < 2: # 현재 방향이 위쪽 or 오른쪽이라면
                tragger_rev_dir[curr_x][curr_y] = move_dir + 2 # 역순으로 올 때는 아래쪽 or 왼쪽으로 됨
            else: # 현재 방향이 아래쪽 or 왼쪽이라면
                tragger_rev_dir[curr_x][curr_y] = move_dir - 2 # 역순으로 올 때는 위쪽 or 오른쪽이 됨

            # (0, 0)으로 오게된다면, 즉 한번의 턴이 끝났다면 종료
            if not curr_x and not curr_y:
                break

        # 방향 전환
        move_dir = (move_dir + 1) % 4
        # 만약 현재 방향이 위쪽 or 아래쪽이라면 해당 방향으로 이동 가능한 칸 수를 하나 증가
        if move_dir == 0 or move_dir == 2:
            move_num += 1


# 격자 내에 있는지를 판단
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def runner_move_info(x, y, move_dir):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0] # 좌우하상

    nx = x + dx[move_dir]
    ny = y + dy[move_dir]
    #1. 만약 격자를 벗어난다면 방향을 틀어준다.
    if not in_range(nx, ny):
        if move_dir < 2: # 좌, 우 방향인데 좌 <-> 우, 우 <-> 좌
            move_dir = 1 - move_dir
        else:
            move_dir = 5 - move_dir # 상, 하 방향인데 상 <-> 하, 하 <-> 상
        nx, ny = x + dx[move_dir], y + dy[move_dir]

    #2. 그 다음 위치에 술래가 없다면 움직인다.
    if (nx, ny) != tragger_pos:
        runner_run[nx][ny].append(move_dir)
    # 술래가 있다면 더 움직이지 않음
    else:
        runner_run[x][y].append(move_dir)

def dist_to_trigger(x, y):
    # 현재 술래의 위치 x,y로 저장
    tragger_x, tragger_y = tragger_pos # (x,y)
    return abs(tragger_x - x) + abs(tragger_y - y)

def runner_move():
    # 1. runner run 초기화
    for i in range(n):
        for j in range(n):
            runner_run[i][j] = []

    # 2. runner를 전부 움직여준다
    for i in range(n):
        for j in range(n):
            # 술래와의 거리가 3 이내인 runner들에 대해서만 이동
            if dist_to_trigger(i, j) <= 3:
                for move_dir in runner_pos[i][j]:
                    runner_move_info(i, j, move_dir)
            # 그렇지 않다면 현재 위치 그대로 저장
            else:
                for move_dir in runner_pos[i][j]:
                    runner_run[i][j].append(move_dir)

    # Step 3. 술래들의 변한 위치 값을 옮겨담기
    for i in range(n):
        for j in range(n):
            runner_pos[i][j] = runner_run[i][j]


# 현재 술래가 바라보는 방향
def get_tragger_dir():
    # 현재 술래의 위치를 x, y에 저장
    x, y = tragger_pos

    # 어느 방향으로 움직여야 하는지에 대한 정보
    move_dir = 0
    if forward_facing:
        move_dir = tragger_dir[x][y]
    else:
        move_dir = tragger_rev_dir[x][y]

    return move_dir


def check_facing():
    global forward_facing

    # Case 1. 정방향으로 끝에 다다른 경우 방향 바꿔 역방향 시작
    if tragger_pos == (0, 0) and forward_facing:
        forward_facing = False
    # Case 2. 역방향으로 끝에 다다른 경우 방향 바꿔 순방향 시작
    if tragger_pos == (n // 2, n // 2) and not forward_facing:
        forward_facing = True


def tragger_move():
    global tragger_pos

    x, y = tragger_pos #(x,y)

    # 상우하좌 순서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    move_dir = get_tragger_dir()

    # 술래를 한 칸 이동
    tragger_pos = (x + dx[move_dir], y + dy[move_dir])

    # 끝에 도달했다면 방향을 전환해줘야 됨
    check_facing()


def get_score(t):
    global ans

    # 상우하좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 현재 술래의 위치
    x, y = tragger_pos

    # 술래의 방향
    move_dir = get_tragger_dir()

    # 3칸을 바라봅니다.
    for dist in range(3):
        nx, ny = x + dist * dx[move_dir], y + dist * dy[move_dir]

        # 격자를 벗어나지 않으며 나무가 없는 위치라면 도망자들 잡음
        if in_range(nx, ny) and not tree[nx][ny]:
            # 해당 위치의 도망자 수 만큼 점수 획득
            ans += t * len(runner_pos[nx][ny])

            # 잡은 도망자들은 사라짐
            runner_pos[nx][ny] = []

# 변수 선언 및 입력:
n, m, h, k = map(int, input().split()) # n=격자 크기, m=도망자, h=나무 개수 k=턴 수

# 각 칸에 있는 도망자 정보를 관리 (도망자의 방향 저장)
runner_pos = [[[] for _ in range(n)] for _ in range(n)] # 술래의 위치
runner_run = [[[] for _ in range(n)] for _ in range(n)] # 술래가 도망가는 방향
tree = [[False] * n for _ in range(n)] # 나무의 위치

# 정방향 기준으로, 현재 위치에서 술래가 움직여야 할 방향을 관리 (위, 오른쪽, 아래, 왼쪽)
tragger_dir = [[0] * n for _ in range(n)]
# 역방향 기준으로, 현재 위치에서 술래가 움직여야 할 방향을 관리 (아래, 오른쪽, 위쪽, 왼쪽)
tragger_rev_dir = [[0] * n for _ in range(n)]

# 술래의 현재 위치
tragger_pos = (n // 2, n // 2)
# 술래가 움직이는 방향이 정방향이면 True / 아니라면 False
forward_facing = True

ans = 0

# 술래 위치 정보
for _ in range(m):
    x, y, d = map(int, input().split())
    runner_pos[x - 1][y - 1].append(d)

# 나무 위치 정보
for _ in range(h):
    x, y = map(int, input().split())
    tree[x - 1][y - 1] = True

def simulate(t):
    # 1. 도망자 도망
    runner_move()

    # 2. 술래 이동
    tragger_move()

    # 3. 술래잡기 시작
    get_score(t)


# 술래잡기 시작 전에 술래 경로 정보를 미리 계산
initialize_tragger_path()

# 총 k번에 걸쳐 술래잡기 게임 진행
for t in range(1, k + 1):
    simulate(t)

# 정답 출력
print(ans)