import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True

    return False

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                count += 1

    print(count)