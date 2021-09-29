t = int(input())

for i in range(t):
    r, s = map(str, input().split())
    r = int(r)
    for j in s:
        print(j*r,end='')
    print()