a, b, c, m = map(int, input().split())

work = 0
stress = 0
for _ in range(24):
    if stress + a <= m:
        stress += a
        work += b
    else:
        stress = max(stress-c, 0)

print(work)