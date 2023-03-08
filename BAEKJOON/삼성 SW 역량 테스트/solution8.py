from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)] # 0:빈칸, 1:집, 2:치킨집

# 집의 위치, 치킨집의 위치 저장
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        if graph[i][j] == 2:
            chicken.append((i, j))

result = int(1e9) # 최소값을 구해야 되니, 최대값으로 초기화
for c in combinations(chicken, m): # 치킨의 위치 중 m개를 조합으로 구하기
    distance = 0 # 매 조합마다 거리 값 새로 구하기
    for h in house:
        # 각 집의 위치에서 제일 가까운 치킨집 거리 (최소 치킨 거리) 더하기
        distance += min(abs(h[0] - i[0]) + abs(h[1] - i[1]) for i in c)

    result = min(result, distance)

print(result)