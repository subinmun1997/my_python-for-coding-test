def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_next(x, y, d):
    nx = x + dx[d]
    ny = y + dy[d]

    if not in_range(nx, ny):
        d = d+2 if d < 2 else d-2
        nx = x + dx[d]
        ny = y + dy[d]

    return (nx, ny, d)

def find_player(pos):
    for i in range(m):
        _, x, y, _, _, _ = players[i]
        if pos == (x, y):
            return players[i]

    return EMPTY

def update(p):
    num, _, _, _, _, _ = p

    for i in range(m):
        num_i, _, _, _, _, _ = players[i]

        if num == num_i:
            players[i] = p
            break

def move(p, pos):
    num, x, y, d, s, a = p
    nx, ny = pos

    gun[nx][ny].append(a)
    gun[nx][ny].sort(reverse=True)
    a = gun[nx][ny][0]
    gun[nx][ny].pop(0)

    p = (num, nx, ny, d, s, a)
    update(p)

def duel(p1, p2, pos):
    num1, _, _, d1, s1, a1 = p1
    num2, _, _, d2, s2, a2 = p2

    if (s1 + a1, s1) > (s2+ a2, s2):
        points[num1] += (s1 + a1) - (s2 + a2)
        loser_move(p2)
        move(p1, pos)
    else:
        points[num2] += (s2 + a2) - (s1 + a1)
        loser_move(p1)
        move(p2, pos)

def loser_move(p):
    num, x, y, d, s, a = p

    gun[x][y].append(a)
    for i in range(4):
        ndir = (d + i) % 4
        nx = x + dx[ndir]
        ny = y + dy[ndir]

        if in_range(nx, ny) and find_player((nx, ny)) == EMPTY:
            p = (num, x, y, ndir, s, 0)
            move(p, (nx, ny))
            break

EMPTY = (-1, -1, -1, -1, -1, -1)

# n=격자의 크기, m=플레이어의 수, k=라운드의 수
n, m, k = map(int, input().split())

gun = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        if nums[j] != 0:
            gun[i][j].append(nums[j])

players = []
for i in range(m):
    x, y, d, s = map(int, input().split())
    players.append((i, x-1, y-1, d, s, 0))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

points = [0] * m

def simulate():
    for i in range(m):
        num, x, y, d, s, a = players[i]

        nx, ny, ndir = get_next(x, y, d)
        next_player = find_player((nx, ny))

        curr_player = (num, nx, ny, ndir, s, a)
        update(curr_player)

        if next_player == EMPTY:
            move(curr_player, (nx, ny))
        else:
            duel(curr_player, next_player, (nx, ny))


for _ in range(k):
    simulate()

for point in points:
    print(point, end=' ')