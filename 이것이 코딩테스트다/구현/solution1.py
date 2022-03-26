n = int(input())
move_type = list(map(str, input().split()))

x, y = 1, 1 # 현재 위치
direction = ['L','R','U','D']
dx = [0, 0, -1, 1] # L, R, U, D에 따른 이동 방향
dy = [-1, 1, 0, 0]

for move in move_type: # 이동 계획을 하나씩 확인
    for i in range(len(direction)):
        if move == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx >= 1 and nx <= n and ny >= 1 and ny <= n: # 공간을 벗어나지 않는다면
        x = nx
        y = ny

print(x, y)