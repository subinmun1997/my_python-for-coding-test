def dfs(graph, v, visited):
    global answer
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            answer += 1 # 연결되어 있고 방문하지 않았다면 1 증가
            dfs(graph, i, visited)

n = int(input()) # 컴퓨터의 수
m = int(input()) # 연결되어 있는 컴퓨터 쌍의 수

graph = [[] for _ in range(n+1)]

# 컴퓨터 연결 정보 저장
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = 0
visited = [False] * (n+1)
dfs(graph, 1, visited)

print(answer)