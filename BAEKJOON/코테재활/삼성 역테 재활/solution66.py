def initialize_seeker_path(): # 0. 술래가 회전하는 방향 (정방향, 역방향) 기록
    dx = [-1, 0, 1, 0] # 상 우 하 좌
    dy = [0, 1, 0, -1]

    # 술래의 현재 위치
    cur_x, cur_y = seeker_pos
    # 처음 이동 방향은 위쪽, 해당 방향으로 이동하는 횟수
    move_dir, move_num = 0, 1

    # (0, 0)이 아닐 때까지 반복
    while cur_x or cur_y:
        for _ in range(move_num):
            # 정방향일 때 해당 칸에서 이동하는 방향 저장
            seeker_next_dir[cur_x][cur_y] = move_dir
            # 역방향일 때 저장하기 전에, 해당 칸으로 이동
            cur_x, cur_y = cur_x + dx[move_dir], cur_y + dy[move_dir]
            # 역방향일 때는 상 <-> 하, 우 <-> 좌
            seeker_rev_dir[cur_x][cur_y] = move_dir + 2 if move_dir < 2 else move_dir - 2

            # 이동 도중 끝 점에 도달했다면 종료
            if not cur_x and not cur_y:
                break

        # 방향 전환하기
        move_dir = (move_dir + 1) % 4
        # 윗 방향이거나 아래 방향으로 바뀌었다면 이동 가능 횟수 하나 증가시켜주기
        if move_dir == 0 or move_dir == 2:
            move_num += 1

def dist_from_seeker(x, y):
    seeker_x, seeker_y = seeker_pos
    return abs(seeker_x - x) + abs(seeker_y - y)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def hider_move(x, y, move_dir): # 이동 가능한 도망자들 도망 시작
    dx = [0, 0, 1, -1] # 좌 우 하 상
    dy = [-1, 1, 0, 0]

    nx = x + dx[move_dir]
    ny = y + dy[move_dir]

    # 격자를 벗어난 경우
    if not in_range(nx, ny):
        # 좌 <-> 우, 하 <-> 상 으로 방향 바꿔주기
        move_dir = 1 - move_dir if move_dir < 2 else 5 - move_dir
        # 바꿔준 방향으로 1칸 움직이기
        nx = x + dx[move_dir]
        ny = y + dy[move_dir]

    # 이동하려는 방향에 술래가 없다면
    if (nx, ny) != seeker_pos:
        next_hiders[nx][ny].append(move_dir)
    # 이동하려는 방향에 술래가 있다면 움직이지 않는다
    else:
        next_hiders[x][y].append(move_dir)

def hiders_move_all(): # 1. 도망자가 이동
    # 도망자 이동 후 위치 매번 새로 저장하기 위해 next 배열 초기화
    for i in range(n):
        for j in range(n):
            next_hiders[i][j] = []

    # 도망자가 이동 가능한지 체크
    for i in range(n):
        for j in range(n):
            # 술래와의 거리가 3 이하인지 체크
            if dist_from_seeker(i, j) <= 3:
                # 3이하가 맞다면 도망 시작
                for move_dir in hiders[i][j]:
                    hider_move(i, j, move_dir)
            # 3이하가 아니라서 도망을 못간다면 그대로 있음
            else:
                for move_dir in hiders[i][j]:
                    next_hiders[i][j].append(move_dir)
    # 옮겨주기
    for i in range(n):
        for j in range(n):
            hiders[i][j] = next_hiders[i][j]

def get_seeker_dir():
    # 술래의 현재 위치
    x, y = seeker_pos

    # 정방향이라면 정방향 위치 저장 배열에서 가져오기
    if forward_facing:
        move_dir = seeker_next_dir[x][y]
    # 역방향이라면 역방향 위치 저장 배열에서 가져오기
    else:
        move_dir = seeker_rev_dir[x][y]

    return move_dir

def check_facing():
    global forward_facing

    # (0, 0)에 정방향으로 도달했다면 역방향으로 바꿔주기
    if seeker_pos == (0, 0) and forward_facing:
        forward_facing = False
    # 정중앙에 역방향으로 도달했다면 정방향으로 바꿔주기
    elif seeker_pos == (n//2, n//2) and not forward_facing:
        forward_facing = True

def seeker_move(): # 2. 술래가 이동
    global seeker_pos

    dx = [-1, 0, 1, 0] # 상 우 하 좌
    dy = [0, 1, 0, -1]

    # 술래의 현재 좌표 가져오기
    x, y = seeker_pos
    # 술래가 이동할 방향 가져오기
    move_dir = get_seeker_dir()

    # 술래 한 칸 움직여주기
    seeker_pos = (x + dx[move_dir], y + dy[move_dir])

    # 끝에 도달했는지 체크
    check_facing()

def get_score(t): # 3. 점수 획득
    global answer

    dx = [-1, 0, 1, 0] # 상 우 하 좌
    dy = [0, 1, 0, -1]

    # 현재 술래의 위치
    x, y = seeker_pos

    # 현재 술래의 방향
    move_dir = get_seeker_dir()

    # 술래가 바라보는 방향으로 3칸 내다본다
    for dist in range(3):
        nx = x + dist * dx[move_dir]
        ny = y + dist * dy[move_dir]

        # 범위 내이고, 나무가 없다면 도망자 잡기
        if in_range(nx, ny) and not tree[nx][ny]:
            answer += t * len(hiders[nx][ny])
            # 잡힌 도망자는 없애주기
            hiders[nx][ny] = []

# n=격자 크기, m=도망자 수, h=나무의 수, k=턴의 수
n, m, h, k = map(int, input().split())

# 도망자의 현재 위치 정보
hiders = [[[] for _ in range(n)] for _ in range(n)]
# 도망자의 이동 후 위치 정보
next_hiders = [[[] for _ in range(n)] for _ in range(n)]
# 나무의 존재 여부
tree = [[False] * n for _ in range(n)]

# 술래의 처음 위치 (정중앙)
seeker_pos = (n//2, n//2)
# 정방향이면 True, 역방향이면 False
forward_facing = True

# 술래의 순방향 이동 정보
seeker_next_dir = [[0] * n for _ in range(n)]
# 술래의 역방향 이동 정보
seeker_rev_dir = [[0] * n for _ in range(n)]

# 도망자의 위치와 이동 방법
for _ in range(m):
    x, y, d = map(int, input().split())
    # 도망자가 있는 해당 위치에 이동 방법 저장
    hiders[x-1][y-1].append(d)

# 나무의 위치
for _ in range(h):
    x, y = map(int, input().split())
    tree[x-1][y-1] = True

# 출력 조건: k번의 턴 동안 술래가 얻는 총 점수
answer = 0
def simulate(t): # k번의 턴 동안 반복 함수
    # 1. 도망자가 이동
    hiders_move_all()

    # 2. 술래가 이동
    seeker_move()

    # 3. 점수 획득하기
    get_score(t)

# 술래의 이동 정보(정방향, 역방향) 사전에 기록해놓기
initialize_seeker_path()

for t in range(1, k+1):
    simulate(t)

# 얻은 총 점수 출력
print(answer)