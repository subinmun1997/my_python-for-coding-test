def rev(n):
    n = str(n)[::-1]
    return int(n)

x, y = map(int, input().split())
result = rev(x) + rev(y)
print(rev(result))

