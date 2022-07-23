n = int(input())
point = sorted(list(map(int, input().split())) for _ in range(n))

for i in point:
    print(*i)