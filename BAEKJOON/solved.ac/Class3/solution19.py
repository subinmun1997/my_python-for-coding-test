import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

count = 0
def dfs(graph, v, visited):
    global count
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)

    return count

result = dfs(graph, 1, visited)
print(result)


