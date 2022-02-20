n = int(input())
array = [[0] * 1001 for _ in range(1001)]

for k in range(1, n+1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        for j in range(y, y+h):
            array[i][j] = k

for i in range(1, n+1):
    cnt = 0
    for r in range(1001):
        cnt += array[r].count(i)
    print(cnt)