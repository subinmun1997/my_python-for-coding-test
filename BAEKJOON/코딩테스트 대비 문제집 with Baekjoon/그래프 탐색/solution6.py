n = int(input())
k = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

answer = 0
def dfs(graph, v, visited):
    global answer
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            answer += 1
            dfs(graph, i, visited)
    return answer

for _ in range(k):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = dfs(graph, 1, visited)
print(result)
