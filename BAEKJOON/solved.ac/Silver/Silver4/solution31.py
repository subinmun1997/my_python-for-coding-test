n, k = map(int, input().split())
number = [i for i in range(2, n+1)]
check = [True, True] + [False] * (n-1)

count = 0
flag = False
for i in range(2, n+1):
    for j in range(i, n+1, i):
        if not check[j]:
            check[j] = True
            count += 1
        if count == k:
            flag = True
            print(j)
            break
    if flag:
        break
