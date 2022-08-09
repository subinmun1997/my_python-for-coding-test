n, k = map(int, input().split())
result = 0

flag = [True] * (n+1)
for i in range(2, n+1):
    for j in range(i, n+1, i):
        if flag[j] != False:
            flag[j] = False
            result += 1
            if result == k:
                print(j)