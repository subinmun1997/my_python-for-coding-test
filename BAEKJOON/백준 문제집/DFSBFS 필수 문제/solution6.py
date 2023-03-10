def dfs(v, num):
    num += 1 # 깊이가 깊어질 때 num+1 해주기
    visited[v] = True

    if v == b: # v값이 찾고자 하는 b값과 동일하다면 result에 저장하기
        result.append(num)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
# 노드들의 연결 정보 저장
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
result = []

dfs(a, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)