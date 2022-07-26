t = int(input())
dp = [1,1,1,2,2,3,4,5,7,9]
for i in range(10, 101):
    dp.append(dp[i-3] + dp[i-2])

for _ in range(t):
    n = int(input())
    print(dp[n-1])