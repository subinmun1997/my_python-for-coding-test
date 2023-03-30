def dfs(depth, idx):
    global result

    if depth == m:
        # 선택된 치킨집들만 따로 저장
        safe_chicken = [chicken[i] for i in range(len(chicken)) if safe[i]]
        distance = 0
        for h in house:
            distance += min(abs(h[0] - j[0]) + abs(h[1] - j[1]) for j in safe_chicken)
        result = min(result, distance)
        return

    for i in range(idx, len(safe)):
        if not safe[i]:
            safe[i] = True
            dfs(depth+1, i+1)
            safe[i] = False

# 입력 조건
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house = [] # 집의 위치
chicken = [] # 치킨집 위치
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

# 선택된 치킨집을 True로 바꿔주기 위한 false 배열
safe = [False] * len(chicken)
result = int(1e9)
dfs(0, 0)

print(result)