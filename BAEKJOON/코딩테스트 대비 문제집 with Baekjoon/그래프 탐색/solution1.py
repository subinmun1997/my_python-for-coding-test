n = int(input())
pair = int(input())
computer = [[] for _ in range(n+1)]

count = 0
def dfs(array, v, visited):
    global count
    visited[v] = True
    for i in array[v]:
        if not visited[i]:
            count += 1
            dfs(array, i, visited)
    return count

for _ in range(pair):
    x, y = map(int, input().split())
    computer[x].append(y)
    computer[y].append(x)
visited = [False] * (n+1)
result = dfs(computer, 1, visited)
print(result)