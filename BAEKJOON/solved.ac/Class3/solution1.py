t = int(input())

for _ in range(t):
    n = int(input())

    dp0 = [1, 0, 1]
    for i in range(3, n+1):
        dp0.append(dp0[i-1] + dp0[i-2])

    dp1 = [0, 1, 1]
    for i in range(3, n+1):
        dp1.append(dp1[i-1] + dp1[i-2])

    print(dp0[n], dp1[n])