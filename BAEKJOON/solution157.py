n, k = map(int, input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
w = [0]
v = [0]

for i in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = w[i]
        value = v[i]
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-weight]+value, dp[i-1][j])
print(dp[n][k])
