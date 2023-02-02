import sys
from copy import deepcopy
input = sys.stdin.readline

def dust_in(x, y):
    temp = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
            temp += (graph[nx][ny] // 5)

    return temp

def dust_out(x, y):
    temp = 0
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
            cnt += 1

    temp += (graph[x][y] // 5) * cnt
    return temp

def air_clean(graph, new_graph):
    #위쪽 반시계
    graph[air-1][1] = 0
    for i in range(2, c):
        graph[air-1][i] = new_graph[air-1][i-1]

    for i in range(air-1):
        graph[i][-1] = new_graph[i+1][-1]

    for i in range(c-1):
        graph[0][i] = new_graph[0][i+1]

    for i in range(1, air-1):
        graph[i][0] = new_graph[i-1][0]

    for i in range(1, air-1):
        for j in range(1, c-1):
            graph[i][j] = new_graph[i][j]

    #아래쪽 시계
    graph[air][1] = 0
    for i in range(2, c):
        graph[air][i] = new_graph[air][i-1]

    for i in range(air+1, r):
        graph[i][-1] = new_graph[i-1][-1]

    for i in range(c-1):
        graph[r-1][i] = new_graph[r-1][i+1]

    for i in range(air+1, r-1):
        graph[i][0] = new_graph[i+1][0]

    for i in range(air+1, r-1):
        for j in range(1, c-1):
            graph[i][j] = new_graph[i][j]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r, c, t = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))

air = 0
for i in range(r):
    if graph[i][0] == -1:
        air = i + 1
        break

for _ in range(t):
    new_graph = deepcopy(graph)
    for i in range(r):
        for j in range(c):
            if graph[i][j] != -1:
                total_dus = (dust_in(i, j) - dust_out(i, j))
                new_graph[i][j] += total_dus
    air_clean(graph, new_graph)

result = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] != -1:
            result += graph[i][j]

print(result)