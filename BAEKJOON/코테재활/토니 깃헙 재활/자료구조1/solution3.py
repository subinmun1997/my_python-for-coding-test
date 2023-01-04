t = int(input())
for _ in range(t):
    ps = input()

    while '()' in ps:
        ps = ps.replace('()', '')
    if ps:
        print("NO")
    else:
        print("YES")