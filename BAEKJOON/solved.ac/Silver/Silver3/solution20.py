n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if i + schedule[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(schedule[i][1] + dp[i+schedule[i][0]], dp[i+1])

print(max(dp))