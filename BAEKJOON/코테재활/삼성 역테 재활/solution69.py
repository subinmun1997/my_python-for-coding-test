def initialize_seeker_path():
    dx = [-1, 0, 1, 0] # 상 우 하 좌
    dy = [0, 1, 0, -1]

    # 술래의 시작 위치
    cur_x, cur_y = n//2, n//2
    move_dir, move_num = 0, 1

    while cur_x or cur_y:
        for _ in range(move_num):
            seeker_move_dir[cur_x][cur_y] = move_dir
            cur_x = cur_x + dx[move_dir]
            cur_y = cur_y + dy[move_dir]
            seeker_rev_dir[cur_x][cur_y] = move_dir + 2 if move_dir < 2 else move_dir - 2

            if not cur_x and not cur_y:
                break

        move_dir = (move_dir + 1) % 4
        if move_dir == 0 or move_dir == 2:
            move_num += 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def hider_move(x, y, move_dir):
    dx = [0, 0, -1, 1] # 좌 우 상 하
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
    # 현재 술래의 위치와 도망자의 위치의 차이 반환
    return abs(x - seeker_x) + abs(y - seeker_y)

def hiders_move_all():
    # 도망자를 이동시키기 전에 이동 후 위치를 초기화 해주기
    for i in range(n):
        for j in range(n):
            next_hiders[i][j] = []

    for i in range(n):
        for j in range(n):
            # 술래와의 거리가 3이하인 도망자들만 이동
            if dist_from_seeker(i, j) <= 3:
                for move_dir in hiders[i][j]:
                    hider_move(i, j, move_dir)
            # 술래와의 거리가 3이하가 아니라면 이동하지 않음
            else:
                for move_dir in hiders[i][j]:
                    next_hiders[i][j].append(move_dir)

    # 이동한 값 원래 도망자 배열로 옮겨주기
    for i in range(n):
        for j in range(n):
            hiders[i][j] = next_hiders[i][j]

def get_seeker_dir():
    x, y = seeker_pos

    if forward_facing:
        move_dir = seeker_move_dir[x][y]
    else:
        move_dir = seeker_rev_dir[x][y]

    return move_dir

def check_facing():
    global forward_facing

    if seeker_pos == (0, 0) and forward_facing:
        forward_facing = False
    elif seeker_pos == (n//2, n//2) and forward_facing:
        forward_facing = True

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

# 입력 조건
# n=격자의 크기, m=도망자의 수, h=나무의 수, k=턴의 수
n, m, h, k = map(int, input().split())

# 도망자의 현재 위치
hiders = [[[] for _ in range(n)] for _ in range(n)]
# 도망자의 이동 후 위치
next_hiders = [[[] for _ in range(n)] for _ in range(n)]
# 나무의 존재 여부
tree = [[False] * n for _ in range(n)]

# 정방향일 때 술래의 이동 방향
seeker_move_dir = [[0] * n for _ in range(n)]
# 역방향일 때 술래의 이동 방향
seeker_rev_dir = [[0] * n for _ in range(n)]

# 술래의 현 위치
seeker_pos = (n//2, n//2)
# 정방향일 때는 True, 역방향일 때는 False
forward_facing = True

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(m):
    x, y, d = map(int, input().split())
    hiders[x-1][y-1].append(d)

for _ in range(h):
    x, y = map(int, input().split())
    tree[x-1][y-1] = True


answer = 0
def simulate(t):
    # 1. 도망자의 이동
    hiders_move_all()

    # 2. 술래의 이동
    seeker_move()

    # 3. 점수 얻기
    get_score(t)


initialize_seeker_path()

for t in range(1, k+1):
    simulate(t)

print(answer)