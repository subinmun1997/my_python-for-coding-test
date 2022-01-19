n, m = map(int, input().split())

if n < m:
    value = m-n
else:
    value = n-m

if value > 0:
    print(value)
else:
    print(-value)