n, l = map(int, input().split())
height = sorted(list(map(int, input().split())))

for i in height:
    if i <= l:
        l += 1

print(l)