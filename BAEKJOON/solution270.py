n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())
    count = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            count += graph[a][b]

    print(count)