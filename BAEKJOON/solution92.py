t = int(input())


for _ in range(t):
    x, y = 1, 1
    h, w, n = map(int, input().split())
    while n > h:
        n -= h
        y += 1
    if n <= h:
        x += (n-1)

    if y < 10:
        y = '0' + str(y)
    else:
        y = str(y)
    print(str(x)+y)

