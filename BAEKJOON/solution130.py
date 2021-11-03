import sys
t = int(sys.stdin.readline())

for i in range(0, t):
    count = 1
    a = []
    n = int(sys.stdin.readline())

    a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    a.sort()
    m = a[0][1]
    print(m)

    for i in range(1, n):
        if m > a[i][1]:
            count += 1
            m = a[i][1]
    print(count)