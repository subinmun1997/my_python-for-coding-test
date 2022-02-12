n, k, l = map(int, input().split())

vip = []
team = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if min(a,b,c) >= l and a+b+c >= k:
        vip.append((a, b, c))
        team += 1

print(team)
for v in vip:
    for i in v:
        print(i, end=' ')
