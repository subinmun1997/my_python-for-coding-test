a, b, c, m = map(int, input().split())

work = 0
stress = 0
for i in range(24):
    if stress + a <= m:
        stress += a
        work += b
    else:
        stress -= c
        if stress < 0:
            stress = 0

print(work)