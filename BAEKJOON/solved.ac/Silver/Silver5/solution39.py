n, m = map(int, input().split())
matrixA = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
matrixB = [list(map(int, input().split())) for _ in range(m)]

result = [[0 for _ in range(k)] for _ in range(n)]
for x in range(n):
    for y in range(k):
        for z in range(m):
            result[x][y] += matrixA[x][z] * matrixB[z][y]

for i in result:
    print(*i)