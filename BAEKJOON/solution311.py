a, b = map(int, input().split())
c = int(input())

x = a
y = b+c

if y >= 60:
    x += (y // 60)
    y %= 60

if x >= 24:
    x %= 24

print(x, y)