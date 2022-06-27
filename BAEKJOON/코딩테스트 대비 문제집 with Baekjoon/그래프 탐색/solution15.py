computer = int(input())
conn = int(input())
graph = [[] for _ in range(computer+1)]

for _ in range(conn):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = 0
def dfs(graph, v, visited):
    global answer
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            answer += 1
            dfs(graph, i, visited)

    return answer

visited = [False] * (computer + 1)

result = dfs(graph, 1, visited)
print(result)