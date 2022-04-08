from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
answer = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                answer[i] = v
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)

for i in range(2, n+1):
    print(answer[i])