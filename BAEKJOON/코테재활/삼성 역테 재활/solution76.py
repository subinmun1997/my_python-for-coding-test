n = int(input())
# 각 날의 (상담일수, 금액)
schedule = [list(map(int, input().split())) for _ in range(n)]
cost = [0] * (n+1)

for d in range(n-1, -1, -1):
    # 날이 넘어가서 상담을 할 수 없다면
    if d + schedule[d][0] > n:
        # 수익에는 변동 없음
        cost[d] = cost[d+1]
    # 상담을 할 수 있다면
    else:
        # max(현재 상담을 하고 끝난 후 다른 상담까지 했을 때 받는 금액, 다음 상담으로 받는 금액)
        cost[d] = max(schedule[d][1] + cost[d + schedule[d][0]], cost[d+1])

# 얻을 수 있는 최대 이익
print(max(cost))