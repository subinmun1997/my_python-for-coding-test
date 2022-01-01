n = int(input())
route = list(map(str, input().split()))

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direction = ['L','R','U','D']

for r in route:
    for i in range(4):
        if r == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x = nx
    y = ny

print(x,y)