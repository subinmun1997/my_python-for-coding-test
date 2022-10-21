n = int(input())

for _ in range(n):
    ps = input()

    while '()' in ps:
        ps = ps.replace('()', '')

    if len(ps):
        print("NO")
    else:
        print("YES")