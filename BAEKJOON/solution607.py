n, a, d = map(int, input().split())
melody = list(map(int, input().split()))

x = 0
for i in range(n):
    if melody[i] == a:
        x += 1
        a += d

print(x)