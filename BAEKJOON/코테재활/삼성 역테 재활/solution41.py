from itertools import combinations

# 입력 조건
n, m = map(int, input().split())
# 0=빈 칸, 1=집, 2=치킨집
graph = [list(map(int, input().split())) for _ in range(n)]

home = [] # 집 위치
chicken = [] # 치킨집 위치
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

# 출력 조건
result = int(1e9)
# 치킨집 m개의 조합을 각각 살펴보며
for c in combinations(chicken, m):
    temp = 0
    for h in home:
        # 집과 가장 가까운(거리가 min값인) 치킨집 더해주기
        temp += min(abs(h[0] - i[0]) + abs(h[1] - i[1]) for i in c)
    result = min(result, temp)

print(result)