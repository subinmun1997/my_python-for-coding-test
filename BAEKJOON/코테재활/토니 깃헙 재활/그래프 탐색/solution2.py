from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)

count = 0
def bfs(graph, start, visited):
    global count
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                count += 1
                visited[i] = True
                queue.append(i)

bfs(graph, 1, visited)
print(count)