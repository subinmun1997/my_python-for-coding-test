def move(dir):
    # 원래 주사위의 각 값 대입
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if dir == 1: # 동쪽으로 이동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 2: # 서쪽으로 이동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 3: # 북쪽으로 이동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
    elif dir == 4: # 남쪽으로 이동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b


    # 입력 조건
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

# 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.
dice = [0, 0, 0, 0, 0, 0] # 위 앞 오른쪽 왼쪽 뒤 아래

dx = [0, 0, -1, 1] # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.
dy = [1, -1, 0, 0]

nx, ny = x, y
for i in order:
    nx += dx[i-1] # 이동한 방향만큼 더해줌
    ny += dy[i-1]

    # 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령 무시, 그리고 전 칸으로 돌려줌
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue

    move(i)
    if board[nx][ny] == 0: # 이동한 칸에 쓰여 있는 수가 0이면
        # 주사위의 바닥면에 쓰여 있는 수가 칸에 복사됨
        board[nx][ny] = dice[-1]
    else:
        # 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0 # 칸에 쓰여 있는 수는 0이 된다.

    # 매 명령마다 주사위가 이동했을 때의 상단에 쓰여진 값 출력
    print(dice[0])