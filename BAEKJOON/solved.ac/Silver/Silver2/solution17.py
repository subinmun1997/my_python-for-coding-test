
def dfs(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False

    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y-1)
        dfs(x-1, y+1)
        dfs(x+1, y-1)
        dfs(x+1, y+1)
        return True
    return False

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                result += 1

    print(result)