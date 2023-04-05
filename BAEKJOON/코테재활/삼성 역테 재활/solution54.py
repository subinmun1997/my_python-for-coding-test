def initialize_seeker_path():
    dx = [-1, 0, 1, 0] # 상 우 하 좌
    dy = [0, 1, 0, -1]

    # 현재 시작 위치
    cur_x, cur_y = n//2, n//2
    # 이동 방향, 해당 방향으로 이동하는 횟수
    move_dir, move_num = 0, 1

    while cur_x or cur_y:
        for _ in range(move_num):
            seeker_next_dir[cur_x][cur_y] = move_dir
            cur_x = cur_x + dx[move_dir]
            cur_y = cur_y + dy[move_dir]
            seeker_rev_dir[cur_x][cur_y] = move_dir + 2 if move_dir < 2 else move_dir - 2

            # (0, 0)에 도착하면
            if not cur_x and not cur_y:
                break

        move_dir = (move_dir + 1) % 4
        if move_dir == 0 or move_dir == 2:
            move_num += 1

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def hider_move(x, y, move_dir):
    dx = [0, 0, 1, -1] # 좌 우 하 상
    dy = [-1, 1, 0, 0]

    nx = x + dx[move_dir]
    ny = y + dy[move_dir]

    if not in_range(nx, ny):
        move_dir = 1 - move_dir if move_dir < 2 else 5 - move_dir
        nx = x + dx[move_dir]
        ny = y + dy[move_dir]

    if (nx, ny) != seeker_pos:
        next_hiders[nx][ny].append(move_dir)
    else:
        next_hiders[x][y].append(move_dir)

def dist_from_seeker(x, y):
    seeker_x, seeker_y = seeker_pos
    return abs(seeker_x - x) + abs(seeker_y - y)

def hiders_move_all():
    for i in range(n):
        for j in range(n):
            next_hiders[i][j] = []

    for i in range(n):
        for j in range(n):
            if dist_from_seeker(i, j) <= 3:
                for move_dir in hiders[i][j]:
                    hider_move(i, j, move_dir)
            else:
                for move_dir in hiders[i][j]:
                    next_hiders[i][j].append(move_dir)

    for i in range(n):
        for j in range(n):
            hiders[i][j] = next_hiders[i][j]

def get_seeker_dir():
    x, y = seeker_pos

    if forward_forcing:
        move_dir = seeker_next_dir[x][y]
    else:
        move_dir = seeker_rev_dir[x][y]

    return move_dir

def check_facing():
    global forward_forcing

    if seeker_pos == (0, 0) and forward_forcing:
        forward_forcing = False
    if seeker_pos == (n//2, n//2) and not forward_forcing:
        forward_forcing = True

def seeker_move():
    global seeker_pos

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    x, y = seeker_pos
    move_dir = get_seeker_dir()

    seeker_pos = (x + dx[move_dir], y + dy[move_dir])

    check_facing()

def get_score(t):
    global answer

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    x, y = seeker_pos
    move_dir = get_seeker_dir()

    for dist in range(3):
        nx = x + dist * dx[move_dir]
        ny = y + dist * dy[move_dir]

        if in_range(nx, ny) and not tree[nx][ny]:
            answer += t * len(hiders[nx][ny])
            hiders[nx][ny] = []

# n=격자의 크기, m=도망자의 수, h=나무의 수, k=턴의 수
n, m, h, k = map(int, input().split())

# 도망자의 현재 위치 (해당 위치에 도망자의 이동 방향만 저장한다)
hiders = [[[] for _ in range(n)] for _ in range(n)]
# 도망자가 이동한 뒤의 위치 (마찬가지로 해당 위치에 도망자의 이동 방향만 저장한다)
next_hiders = [[[] for _ in range(n)] for _ in range(n)]
# 나무의 위치 저장 (나무의 유무로 bool 값)
tree = [[False] * n for _ in range(n)]

# 술래의 이동방향 (정방향)
seeker_next_dir = [[0 for _ in range(n)] for _ in range(n)]
# 술래의 이동방향 (역방향)
seeker_rev_dir = [[0 for _ in range(n)] for _ in range(n)]
# 술래의 현 위치
seeker_pos = (n//2, n//2)
# 정방향이면 True, 역방향이면 False
forward_forcing = True

# 도망자의 위치
for _ in range(m):
    x, y, d = map(int, input().split())
    hiders[x-1][y-1].append(d)

# 나무의 위치
for _ in range(h):
    x, y = map(int, input().split())
    tree[x-1][y-1] = True

def simulation(t):
    # 1. 도망자 이동
    hiders_move_all()

    # 2. 술래 이동
    seeker_move()

    # 3. 점수 획득
    get_score(t)

# 술래잡기 시작 전에 술래의 이동 경로 저장
initialize_seeker_path()

answer = 0
for t in range(1, k+1):
    simulation(t)

print(answer)