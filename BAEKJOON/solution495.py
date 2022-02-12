n, l = map(int, input().split())
friuts = sorted(list(map(int, input().split())))

for f in friuts:
    if f <= l:
        l += 1

print(l)

