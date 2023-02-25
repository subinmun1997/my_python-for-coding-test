n = int(input())
order = list(input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

x, y = 0, 0
for i in order:
    for j in range(4):
        if move[j] == i:
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < n and 0 <= ny < n:
                x, y = nx, ny

print(x+1, y+1)