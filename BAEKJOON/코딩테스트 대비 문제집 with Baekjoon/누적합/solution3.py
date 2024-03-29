n = int(input())
numbers = list(map(int, input().split()))

dp = [-1001] * n
dp[0] = max(dp[0], numbers[0])
for i in range(1, n):
    dp[i] = max(dp[i], numbers[i], dp[i-1]+numbers[i])

print(max(dp))
