from collections import deque

def bfs(graph, start, visited):
    global answer

    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                answer += 1
                visited[i] = True
                queue.append(i)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = 0
visited = [False] * (n+1)
bfs(graph, 1, visited)

print(answer)