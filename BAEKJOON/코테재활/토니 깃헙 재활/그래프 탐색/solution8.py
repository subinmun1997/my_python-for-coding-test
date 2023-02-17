n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = 0
# DFS 방법으로 그래프 탐색하며 연결되어 있는 컴퓨터 수 구하기
def dfs(graph, v, visited):
    global result
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            result += 1
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(result)