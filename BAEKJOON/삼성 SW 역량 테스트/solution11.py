import sys
input = sys.stdin.readline

def spring_summer():
    for x in range(n):
        for y in range(n):
            if live[x][y]:
                live[x][y].sort()
                temp_live_tree = []
                depth = 0
                for age in live[x][y]:
                    if age <= origin_oil[x][y]:
                        origin_oil[x][y] -= age
                        age += 1
                        temp_live_tree.append(age)
                    else:
                        depth += age // 2

                origin_oil[x][y] += depth
                live[x][y] = []
                live[x][y].extend(temp_live_tree)

def fall():
    for x in range(n):
        for y in range(n):
            if live[x][y]:
                for age in live[x][y]:
                    if age % 5 == 0:
                        for dir in range(8):
                            nx = x + dx[dir]
                            ny = y + dy[dir]

                            if 0 <= nx < n and 0 <= ny < n:
                                live[nx][ny].append(1)

def winter():
    for x in range(n):
        for y in range(n):
            origin_oil[x][y] += plus_oil[x][y]

n, m, k = map(int, input().split())
plus_oil = []
for _ in range(n):
    plus_oil.append(list(map(int, input().split())))

origin_oil = [[5 for _ in range(n)] for _ in range(n)]
live = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    live[x-1][y-1].append(z)

dx = [-1, 0, 1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

for _ in range(k):
    spring_summer()
    fall()
    winter()

result = 0
for i in range(n):
    for j in range(n):
        result += len(live[i][j])

print(result)