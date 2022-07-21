t = int(input())

for _ in range(t):
    k = int(input())

    dp0 = [1, 0, 1]
    for i in range(3, k+1):
        dp0.append(dp0[i-1] + dp0[i-2])

    dp1 = [0, 1, 1]
    for i in range(3, k+1):
        dp1.append(dp1[i-1] + dp1[i-2])

    print(dp0[k], dp1[k])