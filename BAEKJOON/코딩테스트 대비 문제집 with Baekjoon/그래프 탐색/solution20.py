from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)

def bfs(start):
    visited = [False] * (n+1)
    visited[start] = True
    count = 1
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                count += 1
                queue.append(i)
                visited[i] = True
    return count

answer = []
max_cnt = 0
for i in range(1, n+1):
    temp = bfs(i)
    if max_cnt == temp:
        answer.append(i)
    elif temp > max_cnt:
        max_cnt = temp
        answer = []
        answer.append(i)

print(*answer)