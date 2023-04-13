def dfs(x, y):
    global cnt

    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

# 총 단지수
village = 0
# 각 단지내 집의 수
home = []
cnt = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            village += 1
            home.append(cnt)
            cnt = 0

print(village)
for h in sorted(home):
    print(h)