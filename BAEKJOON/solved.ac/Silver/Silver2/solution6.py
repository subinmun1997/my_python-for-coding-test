import sys
sys.setrecursionlimit(10000)

t = int(input())

def dfs(x, y):
    if 0 <= x < n and 0 <= y < m:
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
    return False

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                count += 1

    print(count)