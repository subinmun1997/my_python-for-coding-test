def dfs(depth, idx):
    global result
    # n//2명씩 팀이 구성 됐으면
    if depth == n//2:
        # 스타트 팀 능력치 초기화
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                # 둘 다 true 값이라면 둘이 한 팀
                if visited[i] and visited[j]:
                    start += graph[i][j]
                # 둘 다 false 값이라면 둘이 한 팀
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]
        # 능력치 차이의 최솟값 갱신
        result = min(result, abs(start - link))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

# 입력 값
n = int(input())
# 능력치
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]

# 두 팀의 능력치의 차이의 최소값
result = int(1e9)
dfs(0, 0)

print(result)