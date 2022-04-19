n = int(input())
board = [list(input()) for _ in range(n)]
play = [list(input()) for _ in range(n)]
result = [['.'] * n for _ in range(n)]

dx = [-1, 0, 1, 0, -1, 1, 1, -1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]

for x in range(n):
    for y in range(n):
        if board[x][y] == '.' and play[x][y] == 'x':
            count = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if board[nx][ny] == '*':
                    count += 1
            result[x][y] = count

        if board[x][y] == '*' and play[x][y] == 'x':
            for a in range(n):
                for b in range(n):
                    if board[a][b] == '*':
                        result[a][b] = '*'

for i in range(n):
    for j in range(n):
        print(result[i][j], end='')
    print()

