# 정중앙으로부터 끝까지 움직이는 경로를 계산
def initialize_seeker_path():
    dx = [-1, 0, 1, 0] # 위 오른쪽 아래 왼쪽
    dy = [0, 1, 0, -1]

    # 시작 위치와 방향
    cur_x, cur_y = n//2, n//2
    # 해당 방향으로 이동할 횟수 설정(처음에는 윗 방향으로 가니 0으로 설정)
    move_dir, move_num = 0, 1

    # (0,0)이 아닐 때까지 반복
    while cur_x or cur_y:
        # move_num 만큼 이동
        for _ in range(move_num):
            seeker_next_dir[cur_x][cur_y] = move_dir
            cur_x, cur_y = cur_x + dx[move_dir], cur_y + dy[move_dir]
            # 정방향 오른쪽일 때 -> 역방향은 왼쪽, 정방향 위쪽일 때 -> 역방향은 아래쪽
            seeker_rev_dir[cur_x][cur_y] = move_dir + 2 if move_dir < 2 else move_dir - 2

            # 이동하는 도중 (0, 0)으로 오게 되면, 움직이는 것을 종료
            if not cur_x and not cur_y:
                break

        # 방향 전환
        move_dir = (move_dir + 1) % 4
        # 만약 방향이 위 혹은 아래라면 특정 방향으로 움직여야 할 횟수를 1 증가시킨다
        if move_dir == 0 or move_dir == 2:
            move_num += 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def hider_move(x, y, move_dir):
    dx = [0, 0, 1, -1] # 좌 우 하 상
    dy = [-1, 1, 0, 0]

    nx = x + dx[move_dir]
    ny = y + dy[move_dir]

    # 1. 만약 격자를 벗어난다면 우선 방향을 틀어준다
    if not in_range(nx, ny):
        # 좌 <-> 우, 하 <-> 상이 되어야 한다
        move_dir = 1 - move_dir if move_dir < 2 else 5 - move_dir
        nx = x + dx[move_dir]
        ny = y + dy[move_dir]

    # 2. 그 다음 위치에 술래가 없다면 움직인다
    if (nx, ny) != seeker_pos:
        next_hiders[nx][ny].append(move_dir)
    # 술래가 있다면 더 움직이지 않는다
    else:
        next_hiders[x][y].append(move_dir)

def dist_from_seeker(x, y):
    seeker_x, seeker_y = seeker_pos
    return abs(seeker_x - x) + abs(seeker_y - y)

def hider_move_all():
    # 1. next hider를 초기화해줌
    for i in range(n):
        for j in range(n):
            next_hiders[i][j] = []

    # 2. hider를 전부 움직여준다
    for i in range(n):
        for j in range(n):
            # 술래와의 거리가 3 이내인 도망자들에 대해서만 움직임
            if dist_from_seeker(i, j) <= 3:
                for move_dir in hiders[i][j]:
                    hider_move(i, j, move_dir)
            # 그렇지 않다면 현재 위치 그대로 넣어준다
            else:
                for move_dir in hiders[i][j]:
                    next_hiders[i][j].append(move_dir)

    # 3. next hider 값을 옮겨준다
    for i in range(n):
        for j in range(n):
            hiders[i][j] = next_hiders[i][j]



# n=격자의 크기, m=도망자, h=나무의 수, k=턴의 수
n, m, h, k = map(int, input().split())

# 각 칸에 있는 도망자 정보 저장
hiders = [[[] for _ in range(n)] for _ in range(n)]
# 도망자가 이동한 후 위치 저장
next_hiders = [[[] for _ in range(n)] for _ in range(n)]
# 나무의 유무
tree = [[False] * n for _ in range(n)]

# 정방향 기준 현재 위치에서 술래가 움직여야 할 방향 관리
seeker_next_dir = [[0] * n for _ in range(n)]
# 역방향 기준 현재 위치에서 술래가 움직여야 할 방향 관리
seeker_rev_dir = [[0] * n for _ in range(n)]

# 술래의 현재 위치
seeker_pos = (n//2, n//2)
# 술래가 움직이는 방향이 정방향이면 True / 아니라면 False
forward_facing = True

answer = 0
# 술래 정보
for _ in range(m):
    x, y, d = map(int, input().split())
    hiders[x-1][y-1].append(d)

for _ in range(h):
    x, y = map(int, input().split())
    tree[x-1][y-1] = True

# 현재 술래가 바라보는 방향을 가져온다
def get_seeker_dir():
    # 현재 술래의 위치를 불러온다
    x, y = seeker_pos

    # 어느 방향으로 움직여야 하는지에 대한 정보를 가져온다
    # 정방향이라면
    if forward_facing:
        move_dir = seeker_next_dir[x][y]
    # 역방향이라면
    else:
        move_dir = seeker_rev_dir[x][y]

    return move_dir

def check_facing():
    global forward_facing

    # 1. 정방향으로 끝에 다다른 경우라면, 방향을 바꿔준다
    if seeker_pos == (0, 0) and forward_facing:
        forward_facing = False
    # 2. 역방향으로 끝에 다다른 경우여도, 방향을 바꿔준다
    if seeker_pos == (n//2, n//2) and not forward_facing:
        forward_facing = True

def seeker_move():
    global seeker_pos

    x, y = seeker_pos

    dx = [-1, 0, 1, 0] # 상 우 하 좌
    dy = [0, 1, 0, -1]

    move_dir = get_seeker_dir()
    # 술래를 한 칸 움직여 준다
    seeker_pos = (x + dx[move_dir], y + dy[move_dir])

    # 끝에 도달했는지 체크하고, 도달했다면 방향을 바꿔줘야 한다
    check_facing()

def get_score(t):
    global answer

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 현재 술래의 위치
    x, y = seeker_pos

    # 현재 술래의 방향
    move_dir = get_seeker_dir()

    # 3칸을 바라본다
    for dist in range(3):
        nx = x + dist * dx[move_dir]
        ny = y + dist * dy[move_dir]

        # 격자를 벗어나지 않으며 나무가 없는 위치라면 도망자들을 전부 잡음
        if in_range(nx, ny) and not tree[nx][ny]:
            # 해당 위치의 도망자 수 만큼 점수를 획득
            answer += t * len(hiders[nx][ny])
            # 도망자들이 사라지게 된다
            hiders[nx][ny] = []

def simulate(t):
    # 1. 도망자가 움직인다
    hider_move_all()
    # 2. 술래가 움직인다
    seeker_move()
    # 3. 점수를 얻는다
    get_score(t)

# 술래잡기 시작 전에, 구현의 편의를 위해 술래의 이동 경로 정보를 미리 계산
initialize_seeker_path()

for t in range(1, k+1):
    simulate(t)

print(answer)