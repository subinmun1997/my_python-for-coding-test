def solution(n):
    dp = [0] * 100001
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567

    return dp[n]

print(solution(3))
print(solution(5))