from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

# n=정점의 개수, m=간선의 개수, v=탐색을 시작할 정점의 번호
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 연결된 간선 정보
# 입력으로 주어지는 간선은 양방향이다
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 방문할 수 있는 정점이 여러 개인 경우에는
# 정점 번호가 작은 것을 먼저 방문한다
for i in range(1, n+1):
    graph[i].sort()

# DFS
visited = [False] * (n+1)
dfs(graph, v, visited)
print()

# BFS
visited = [False] * (n+1)
bfs(graph, v, visited)