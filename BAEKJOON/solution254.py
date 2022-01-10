def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


n, m = map(int, input().split())

data = []
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    data.append((x,y))

for i,j in data:
    if j not in graph[i]:
        graph[i].append(j)
        graph[j].append(i)

visited = [False] * (n+1)
comp = 0
for i in range(1, n+1):
    if visited[i] == False:
        dfs(graph,i,visited)
        comp += 1

print(comp)