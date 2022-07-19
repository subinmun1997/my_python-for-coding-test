t = int(input())

for _ in range(t):
    ps = input()

    while True:
        if '()' in ps:
            ps = ps.replace('()', '')
        else:
            break

    if len(ps) == 0:
        print("YES")
    else:
        print("NO")