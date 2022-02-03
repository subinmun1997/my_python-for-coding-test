m, seed, x1, x2 = map(int, input().split())

for a in range(m):
    found = False
    for c in range(m):
        if (a*seed+c)%m == x1:
            if (a*x1+c)%m == x2:
                print(a, c)
                found = True
                break
    if found:
        break