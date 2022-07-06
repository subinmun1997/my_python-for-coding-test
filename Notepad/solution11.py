n = int(input())
graph = list(map(str, input().split()))

x, y = 1, 1
dx = [0, 0, -1, 1] # L R U D
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for i in graph:
    for j in range(len(move)):
        if move[j] == i:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)