n = int(input())
target = int(input())

dx = [-1, 0, 1, 0] # 상 우 하 좌
dy = [0, 1, 0, -1]

if n%2 == 1:
    x, y = n//2, n//2
else:
    x, y = n//2, n//2 - 1

graph = [[0] * n for _ in range(n)]
graph[x][y] = 1

cnt = 2 # 방향 꺾기
dir = 0 # 상하좌우
next_num = 2 # 다음 숫자

while True:
    for _ in range(cnt-1):
        nx, ny = x + dx[dir], y + dy[dir]
        graph[nx][ny] = next_num
        next_num += 1

        if next_num == n**2 + 1:
            break
        x, y = nx, ny

    if next_num == n**2 + 1:
        break

    dir = (dir+1)%4
    if dir == 0 or dir == 2:
        cnt += 1

for i in graph:
    print(*i)

for i in range(n):
    for j in range(n):
        if graph[i][j] == target:
            print(i+1, j+1)


