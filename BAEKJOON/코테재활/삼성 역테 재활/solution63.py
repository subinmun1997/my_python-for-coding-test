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
                    group_cnt[group_num] += 1
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
                        g_x_cnt, g_y_cnt = group_cnt[g_x], group_cnt[g_y]
                        value += (g_x_cnt + g_y_cnt) * g_x_num * g_y_num

    return value // 2

def plus_rotate():
    for i in range(n):
        for j in range(n):
            if i == half:
                arr[i][j] = pan[j][i]
            elif j == half:
                arr[i][j] = pan[n-j-1][n-i-1]

def square_rotate(x, y, l):
    # 정사각형을 시계방향으로 90' 회전합니다.
    for i in range(x, x+l):
        for j in range(y, y+l):
            # Step 1. (x, y)를 (0, 0)으로 옮겨주는 변환을 진행합니다.
            ox, oy = i-x, j-y
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) -> (y, l - x - 1)가 됩니다.
            rx, ry = oy, l-ox-1
            # Step 3. 다시 (x, y)를 더해줍니다.
            arr[rx+x][ry+y] = pan[i][j]

# 입력 조건
n = int(input())
pan = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0
for i in range(4):
    # 그룹으로 나누기 위한 배열 선언
    group = [[0] * n for _ in range(n)]
    # 나누어진 그룹 별 몇 칸씩 있는지
    group_cnt = [0] * (n * n + 1)
    # 그룹을 나누기 위한 숫자 번호
    group_num = 0
    visited = [[False] * n for _ in range(n)]

    # 그룹 나누기
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                visited[i][j] = True
                group[i][j] = group_num
                group_cnt[group_num] += 1
                group_search(i, j)

    answer += art_score()

    # 회전한 판의 값을 담기 위한 배열
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