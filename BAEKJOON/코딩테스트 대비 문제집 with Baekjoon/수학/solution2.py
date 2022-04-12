a, b, c, m = map(int, input().split())

stress = 0
work = 0
for _ in range(24):
    if stress + a <= m:
        work += b
        stress += a
    else:
        stress -= c
        if stress < 0:
            stress = 0

print(work)