t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))

    p = [False] * n
    p[m] = True

    count = 0
    while True:
        if s[0] == max(s):
            count += 1
            if p[0]:
                print(count)
                break
            else:
                s.pop(0)
                p.pop(0)
        else:
            s.append(s.pop(0))
            p.append(p.pop(0))