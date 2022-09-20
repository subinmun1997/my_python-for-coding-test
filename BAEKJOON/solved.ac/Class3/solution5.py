from collections import deque

def bfs(graph, start, visited):
    num = [0 for _ in range(n+1)]
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for g in graph[v]:
            if not visited[g]:
                num[g] = num[v] + 1
                queue.append(g)
                visited[g] = True

    return sum(num)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = []
for i in range(1, n+1):
    visited = [False] * (n+1)
    result.append(bfs(graph, i, visited))

print(result.index(min(result)) + 1)