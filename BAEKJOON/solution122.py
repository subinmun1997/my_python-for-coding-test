from collections import deque

n = int(input())
k = int(input())

graph = [[] for _ in range(n+1)]
for i in range(k):
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
                global count
                count += 1
                queue.append(i)
                visited[i] = True

    print(count)
count = 0
visited = [False] * (n+1)
bfs(graph,1,visited)