from itertools import combinations

# 입력 값
n = int(input())
# 능력치
graph = [list(map(int, input().split())) for _ in range(n)]
members = [i for i in range(n)]

# 능력치의 차이가 가장 작은 값
result = int(1e9)

# 랜덤으로 n//2명씩 팀 짜기
for r1 in combinations(members, n//2):
    r2 = list(set(members) - set(r1))
    # 스타트 팀, 링크 팀 점수 초기화
    start, link = 0, 0
    # r1팀에서 2명씩 랜덤으로 뽑으며 능력치 더해주기
    for r in combinations(r1, 2):
        start += graph[r[0]][r[1]]
        start += graph[r[1]][r[0]]
    # r2팀에서 2명씩 랜덤으로 뽑으며 능력치 더해주기
    for r in combinations(r2, 2):
        link += graph[r[0]][r[1]]
        link += graph[r[1]][r[0]]

    # 결과값은 기존 값과 두 능력치의 차이 중 더 작은 값으로 갱신
    result = min(result, abs(start - link))

print(result)