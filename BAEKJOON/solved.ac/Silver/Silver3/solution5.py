computer = int(input())
conn = int(input())

graph = [[] for _ in range(computer+1)]
visited = [False] * (computer+1)
for _ in range(conn):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)

    return cnt

answer = dfs(graph, 1, visited)
print(answer)