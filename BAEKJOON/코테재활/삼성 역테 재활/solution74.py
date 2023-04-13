def move(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if dir == 1: # 동쪽으로 굴리기
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, a, f, d, e, b
    if dir == 2: # 서쪽으로 굴리기
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, a, d, e, c
    if dir == 3: # 북쪽으로 굴리기
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, c, f, a, e
    if dir == 4: # 남쪽으로 굴리기
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, b, c, a, f, d

# n=세로, m=가로, (x,y)=좌표, k=명령의 개수
n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 처음 주사위의 모든 면에는 0이 적혀있다
dice = [0, 0, 0, 0, 0, 0] # 위 오른쪽 왼쪽 앞 뒤 아래
order = list(map(int, input().split()))

dx = [0, 0, -1, 1] # 동 서 북 남
dy = [1, -1, 0, 0]

for i in order:
    nx = x + dx[i-1]
    ny = y + dy[i-1]

    # 범위 밖으로 벗어나면 해당 명령 무시
    if not (0 <= nx < n and 0 <= ny < m):
        continue
    # 범위 내로 이동하려는 경우만
    else:
        # 주사위 굴리기
        move(i)
        # 이동한 칸에 쓰여 있는 수가 0이면
        if graph[nx][ny] == 0:
            # 주사위 바닥면에 쓰여 있는 수가 칸에 복사된다
            graph[nx][ny] = dice[-1]
        # 0이 아닌 경우에는
        else:
            # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며
            # 칸에 쓰여 있는 수는 0이 된다
            dice[-1] = graph[nx][ny]
            graph[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])