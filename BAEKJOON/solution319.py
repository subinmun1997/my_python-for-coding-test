import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 10001

dp[0] = 1
dp[1] = 1

for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n-1])