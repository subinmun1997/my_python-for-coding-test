h, m = map(int, input().split())

if m >= 45:
    m -= 45
else:
    m = m - 45 + 60
    h -= 1
if h == -1:
    h = 23

print(h, m)