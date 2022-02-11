t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    result = 0
    for _ in range(n):
        v, f, c = map(int, input().split())
        if f/c * v >= d:
            result += 1

    print(result)