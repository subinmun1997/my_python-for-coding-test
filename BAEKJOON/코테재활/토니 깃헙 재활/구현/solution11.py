n = int(input())
bomb = [list(input()) for _ in range(n)]
play = [list(input()) for _ in range(n)]
answer = [['.'] * n for _ in range(n)]

dx = [-1, 0, 1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

for i in range(n):
    for j in range(n):
        if bomb[i][j] == '.' and play[i][j] == 'x':
            cnt = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if bomb[nx][ny] == '*':
                    cnt += 1
            answer[i][j] = cnt
        elif bomb[i][j] == '*' and play[i][j] == 'x':
            for x in range(n):
                for y in range(n):
                    if bomb[x][y] == '*':
                        answer[x][y] = '*'

for i in range(n):
    for j in range(n):
        print(answer[i][j], end='')
    print()