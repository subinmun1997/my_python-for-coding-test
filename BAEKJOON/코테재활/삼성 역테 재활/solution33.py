'''
백준 15686 치킨 배달 - combinations 풀이
'''
from itertools import combinations

# 입력 조건
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house = [] # 집의 위치 저장
chicken = [] # 치킨집의 위치 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        if graph[i][j] == 2:
            chicken.append((i, j))

result = int(1e9)
# 치킨집 중 m개 고르기
for c in combinations(chicken, m):
    # 매 치킨집 조합마다 거리 새로 구하기
    distance = 0
    for h in house:
        # 치킨 거리가 가장 작게 되는 경우 더하기
        distance += min(abs(h[0] - i[0]) + abs(h[1] - i[1]) for i in c)

    result = min(result, distance)

print(result)