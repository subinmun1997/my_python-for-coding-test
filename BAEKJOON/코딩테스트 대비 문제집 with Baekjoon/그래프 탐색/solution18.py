import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = [[] for _ in range(n+1)]
answer = [0] * (n+1)

for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            answer[i] = v
            dfs(graph, i, visited)

dfs(graph, 1, visited)
for i in range(2, n+1):
    print(answer[i])