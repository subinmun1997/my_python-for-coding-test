from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)

def bfs(start):
    count = 1
    queue = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                count += 1
                queue.append(i)
                visited[i] = True

    return count

result = []
max_cnt = 0
for i in range(1, n+1):
    temp = bfs(i)
    if temp == max_cnt:
        result.append(i)
    elif temp > max_cnt:
        max_cnt = temp
        result = []
        result.append(i)

print(*result)