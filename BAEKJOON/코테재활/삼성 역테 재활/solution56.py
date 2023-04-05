from collections import deque

def group_search(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if pan[nx][ny] == pan[x][y] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    group[nx][ny] = group_num
                    group_count[group_num] += 1
                    queue.append((nx, ny))

def art_score():
    value = 0

    for x in range(n):
        for y in range(n):
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < n and 0 <= ny < n:
                    if group[nx][ny] != group[x][y]:
                        g_x, g_y = group[x][y], group[nx][ny]
                        g_x_num, g_y_num = pan[x][y], pan[nx][ny]
                        g_x_cnt, g_y_cnt = group_count[g_x], group_count[g_y]
                        value += (g_x_cnt + g_y_cnt) * g_x_num * g_y_num

    return value // 2

def plus_rotate():
    for i in range(n):
        for j in range(n):
            if i == half:
                arr[i][j] = pan[j][i]
            if j == half:
                arr[i][j] = pan[n-j-1][n-i-1]

def square_rotate(x, y, l):
    for i in range(x, x+l):
        for j in range(y, y+l):
            ox, oy = i-x, j-y
            rx, ry = oy, l-ox-1
            arr[rx+x][ry+y] = pan[i][j]

n = int(input())
pan = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0
for _ in range(4):
    group = [[0] * n for _ in range(n)]
    group_count = [0] * (n * n + 1)
    group_num = 0
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                group_num += 1
                group[i][j] = group_num
                group_count[group_num] += 1
                group_search(i, j)

    answer += art_score()

    arr = [[0] * n for _ in range(n)]
    half = n // 2

    plus_rotate()

    square_rotate(0, 0, half)
    square_rotate(0, half+1, half)
    square_rotate(half+1, 0, half)
    square_rotate(half+1, half+1, half)

    for i in range(n):
        for j in range(n):
            pan[i][j] = arr[i][j]

print(answer)