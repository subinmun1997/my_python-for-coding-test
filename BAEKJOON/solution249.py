t = int(input())

dp = [0 for _ in range(100)]
dp[0] = dp[1] = dp[2] = 1
dp[3] = dp[4] = 2
dp[5] = 3

for i in range(6, len(dp)):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(t):
    n = int(input())
    print(dp[n-1])
