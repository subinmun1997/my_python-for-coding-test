n = int(input())
graph = [list(map(int, input())) for _ in range(n)]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

        return True

    return False

result = 0
count = 0
home = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            home.append(count)
            result += 1
            count = 0

print(result)
home.sort()
for h in home:
    print(h)