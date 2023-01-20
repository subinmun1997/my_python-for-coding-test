n = int(input())
find = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = n//2, n//2
board[x][y] = 1

next_num = 2
dir = 0
cnt = 2

while True:
    for i in range(cnt - 1):
        nx = x + dx[dir]
        ny = y + dy[dir]
        board[nx][ny] = next_num
        next_num += 1

        if next_num == n ** 2 + 1:
            break
        x, y = nx, ny

    if next_num == n ** 2 + 1:
        break

    dir = (dir + 1) % 4
    if dir == 0 or dir == 2:
        cnt += 1

for i in board:
    print(*i)

for i in range(n):
    for j in range(n):
        if board[i][j] == find:
            print(i+1, j+1)