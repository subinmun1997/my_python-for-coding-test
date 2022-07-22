from collections import deque
n = int(input())
k = int(input())
graph = [[] for _ in range(n+1)]
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

    return count

for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = bfs(graph, 1, visited)
print(answer)