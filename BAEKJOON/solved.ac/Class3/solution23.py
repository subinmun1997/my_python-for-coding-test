n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True

    return False

village = 0
cnt = 0
house = []
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            village += 1
            house.append(cnt)
            cnt = 0

print(village)
house.sort()
for i in house:
    print(i)