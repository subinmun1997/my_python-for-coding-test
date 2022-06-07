n, l = map(int, input().split())
pos = sorted(list(map(int, input().split())))

start = 0
cnt = 0
for p in pos:
    if start < p:
        start = p+l-1
        cnt += 1

print(cnt)