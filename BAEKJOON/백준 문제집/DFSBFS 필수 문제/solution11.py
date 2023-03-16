def dfs(graph, v, visited):
    global count
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            # 1번째 컴퓨터와 연결되어 있으면서 방문한 적이 없다면 +1
            count += 1
            dfs(graph, i, visited)

n = int(input()) # 컴퓨터의 수
m = int(input()) # 연결되어 있는 컴퓨터 쌍의 수

graph = [[] for _ in range(n+1)]
# 연결되어 있는 컴퓨터의 번호 쌍
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

count = 0 # 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수
visited = [False] * (n+1)
dfs(graph, 1, visited)

print(count)