n = int(input())
mirror = [input() for _ in range(n)]
k = int(input())

if k == 1:
    for m in mirror:
        print(m)
elif k == 2:
    for m in mirror:
        print(m[::-1])
else:
    for i in range(n-1,-1,-1):
        print(mirror[i])