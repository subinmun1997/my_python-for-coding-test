n, m = map(int, input().split())
array = [list(input()) for _ in range(n)]

count = 0
while True:
    result = sum(array[i].count('0') for i in range(n))
    if result == n * m:
        break
    for i in range(n):
        for j in range(m):
            if array[i][j] == '1':
                x, y = i, j

    for i in range(x+1):
        for j in range(y+1):
            if array[i][j] == '0':
                array[i][j] = '1'
            else:
                array[i][j] = '0'

    count += 1

print(count)


