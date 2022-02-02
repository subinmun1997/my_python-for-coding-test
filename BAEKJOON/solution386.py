array = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            array[i][j] = 1

count = 0
for row in array:
    count += row.count(1)

print(count)