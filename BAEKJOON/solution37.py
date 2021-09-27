h, m = map(int, input().split())

if m >= 45:
    m -= 45
    print(h,m)
else:
    temp = 45 - m
    m = 60 - temp
    h -= 1
    if h == -1:
        h = 23
    print(h,m)