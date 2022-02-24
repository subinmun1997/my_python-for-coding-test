n = int(input())
direction = []

for _ in range(n):
    x, y = map(str, input().split())
    direction.append((x, int(y)))

location = ['E', 'S', 'W', 'N']
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
x, y = 0, 0

for d,k in direction:
    for i in range(len(location)):
        if d == location[i]:
            nx = x + dx[i] * k
            ny = y + dy[i] * k

            x = nx
            y = ny
print(x, y)