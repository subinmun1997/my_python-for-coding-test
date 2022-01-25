k, n, m = map(int, input().split())
cookies = k * n

if cookies <= m:
    print(0)
else:
    print(cookies-m)