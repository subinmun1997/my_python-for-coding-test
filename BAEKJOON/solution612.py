n = int(input())
mine = [list(input()) for _ in range(n)]
board = [list(input()) for _ in range(n)]
result = [['.'] * n for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for x in range(n):
    for y in range(n):
        if mine[x][y] == '.' and board[x][y] == 'x':
            cnt = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue

                if mine[nx][ny] == "*":
                    cnt += 1
            result[x][y] = cnt

        if mine[x][y] == '*' and board[x][y] == 'x':
            for a in range(n):
                for b in range(n):
                    if mine[a][b] == '*':
                        result[a][b] = '*'

for i in range(n):
    for j in range(n):
        print(result[i][j], end='')

    print()
