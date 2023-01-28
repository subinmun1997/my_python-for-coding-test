def check():
    for start in range(n):
        k = start
        for j in range(h):
            if graph[j][k]:
                k += 1
            elif k > 0 and graph[j][k-1]:
                k -= 1
        if k != start:
            return False
    return True

def dfs(cnt, x, y):
    global result
    if check():
        result = min(result, cnt)
        return
    elif cnt == 3 or result <= cnt:
        return
    for i in range(x, h):
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k, n-1):
            if not graph[i][j] and not graph[i][j+1]:
                if j > 0 and graph[i][j-1]:
                    continue
                graph[i][j] = True
                dfs(cnt+1, i, j+2)
                graph[i][j] = False

n, m, h = map(int, input().split())
graph = [[False] * n for _ in range(h)]

if m == 0:
    print(0)
    exit()
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = True

result = 4
dfs(0, 0, 0)
print(result if result < 4 else -1)