def dfs(f1):
    for i in graph[f1]:
        if not visited[i]:
            visited[i] = visited[f1] + 1
            dfs(i)

# 전체 사람의 수
n = int(input())
# 촌수를 계산해야 하는 서로 다른 두 사람의 번호
f1, f2 = map(int, input().split())
# 부모 자식들 간의 관계의 개수
m = int(input())

graph = [[] for _ in range(n+1)]
# 각 노드간 촌수 계산 배열
visited = [0] * (n+1)

# 노드들간의 연결 정보
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(f1)

# 타켓 위치의 배열 값이 0이 아니라면 촌수 반환, 0이라면 촌수와 관련 없는 것이니 -1 반환
if visited[f2] > 0:
    print(visited[f2])
else:
    print(-1)