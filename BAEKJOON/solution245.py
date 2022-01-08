n = int(input())

s = [0 for _ in range(301)]
dp = [0 for _ in range(301)]
for i in range(n):
    s[i] = int(input())

dp[0] = s[0] # 첫번째 계단
dp[1] = s[0] + s[1] # 두번째 계단
dp[2] = max(s[0]+s[2], s[1]+s[2])

for i in range(3, n):
    dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])

print(dp[n-1])