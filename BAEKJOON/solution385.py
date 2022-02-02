rectangle = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            rectangle[i][j] = 1

answer = 0
for row in rectangle:
    answer += sum(row)
print(answer)
