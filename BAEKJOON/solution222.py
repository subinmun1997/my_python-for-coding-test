def reverse(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]

def check():
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return False
    return True

n, m = map(int, input().split())

A = [list(map(int, input())) for _ in range(n)]
B = [list(map(int, input())) for _ in range(n)]

count = 0

for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            reverse(i, j)
            count += 1

if check():
    print(count)
else:
    print(-1)
