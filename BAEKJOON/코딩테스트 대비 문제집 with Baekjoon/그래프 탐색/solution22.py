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
        dfs(x, y-1)
        dfs(x, y+1)

        return True

    return False

result = 0 # 단지 수
cnt = 0 # 집의 수
answer= []
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            answer.append(cnt)
            result += 1
            cnt = 0

print(result)
answer.sort()
for i in answer:
    print(i)
