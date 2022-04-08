import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
graph = [[] for _ in range(n+1)]
answer = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            answer[i] = v
            dfs(graph, i, visited)

dfs(graph, 1, visited)

for i in range(2, n+1):
    print(answer[i])
