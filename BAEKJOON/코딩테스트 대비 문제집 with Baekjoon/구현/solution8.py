def check(arr):
    cnt = 0
    # 가로
    for i in arr:
        if i.count(0) == 5:
            cnt += 1
    # 세로
    for i in range(5):
        y = 0
        for j in range(5):
            if arr[j][i] == 0:
                y += 1
        if y == 5:
            cnt += 1
    # 대각선(\)
    k = 0
    for i in range(5):
        if arr[i][i] == 0:
            k += 1
    if k == 5:
        cnt += 1
    # 대각선(/)
    u = 0
    for i in range(5):
        if arr[i][4-i] == 0:
            u += 1
    if u == 5:
        cnt += 1

    return cnt

a = []
b = []
for _ in range(5):
    a.append(list(map(int, input().split())))
for _ in range(5):
    w = list(map(int, input().split()))
    for j in w:
        b.append(j)

for idx, num in enumerate(b):
    for m in a:
        if num in m:
            m[m.index(num)] = 0
            break
    res = check(a)
    if res >= 3:
        print(idx + 1)
        break