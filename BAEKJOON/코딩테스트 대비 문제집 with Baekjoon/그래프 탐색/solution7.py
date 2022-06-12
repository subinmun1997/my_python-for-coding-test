from collections import deque

n = int(input())
k = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

cnt = 0
def bfs(graph, start, visited):
    global cnt
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i] = True
    return cnt

for _ in range(k):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = bfs(graph, 1, visited)
print(answer)