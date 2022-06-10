import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    count = 1
    a = []
    n = int(input())

    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort()
    m = a[0][1]

    for i in range(1, n):
        if m > a[i][1]:
            count += 1
            m = a[i][1]
    print(count)