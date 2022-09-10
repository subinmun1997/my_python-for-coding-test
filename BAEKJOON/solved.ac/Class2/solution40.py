n = int(input())

point = [list(map(int, input().split())) for _ in range(n)]
point.sort(key=lambda x : (x[0], x[1]))

for x, y in point:
    print(x, y)