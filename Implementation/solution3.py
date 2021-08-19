input_data = input()

row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]

result = 0
for step in steps:
    new_row = row + step[1]
    new_col = col + step[0]

    if new_row >=1 and new_row <= 8 and new_col >= 1 and new_col <= 8:
        result += 1

print(result)