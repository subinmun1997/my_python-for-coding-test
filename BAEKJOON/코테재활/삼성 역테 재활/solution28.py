from itertools import combinations

# 입력 조건
n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
members = [i for i in range(n)]

result = int(10e9)

#(n//2명의 팀1, n//2명의 팀2)로 임의로 뽑기
for r1 in combinations(members, n//2):
    # 스타트 팀과 링크 팀 점수 초기화
    start, link = 0, 0
    # 전체 멤버 - r1팀 멤버 = r2팀 멤버
    r2 = list(set(members) - set(r1))

    # r1팀 중 2명씩 뽑으며 능력치 계산
    for r in combinations(r1, 2):
        start += ability[r[0]][r[1]]
        start += ability[r[1]][r[0]]

    # r2팀 중 2명씩 뽑으며 능력치 계산
    for r in combinations(r2, 2):
        link += ability[r[0]][r[1]]
        link += ability[r[1]][r[0]]

    # 스타트 팀과 링크 팀의 점수 차이가 최소인 값으로 변경
    result = min(result, abs(start - link))

print(result)
