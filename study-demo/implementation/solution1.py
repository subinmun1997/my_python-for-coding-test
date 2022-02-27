n = int(input())
move = list(map(str, input().split()))

move_type = ['L','R','U','D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x, y = 1, 1
for m in move:
    for i in range(len(move_type)):
        if m == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x = nx
    y = ny

print(x, y)