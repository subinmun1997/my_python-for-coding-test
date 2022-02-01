numbers = []
for i in range(9):
    numbers.append(list(map(int, input().split())))

max_value = 0
for i in range(9):
    for j in range(9):
        if numbers[i][j] > max_value:
            max_value = numbers[i][j]
            row = i
            col = j

print(max_value)
print(row+1, col+1)