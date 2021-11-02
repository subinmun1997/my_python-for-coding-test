import sys

t = int(input())

def dfs(x, y):
    if 0 <= x < n and 0 <= y < m:
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return True
    return False


for _ in range(t):
    m, n, k = map(int, input().split()) # m:가로(열) n:세로(행)
    graph = [[0]*m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1

    print(result)