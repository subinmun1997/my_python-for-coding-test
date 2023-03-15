# 남은 일 수
n = int(input())
# [상담을 완료하는데 걸리는 기간, 받을 수 있는 금액]
schedule = [list(map(int, input().split())) for _ in range(n)]

cost = [0 for _ in range(n+1)] # 결과(최대 이익)
# 마지막날부터 거꾸로 체크하면서 최대이익 찾기
for i in range(n-1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않는다.
    if schedule[i][0] + i > n:
        cost[i] = cost[i+1]
    else:
        # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택
        cost[i] = max(schedule[i][1] + cost[i + schedule[i][0]], cost[i+1])

print(max(cost))