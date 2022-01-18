t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()

    max_level = 0
    for i in range(2, n):
        max_level = max(max_level, abs(l[i] - l[i-2]))

    print(max_level)