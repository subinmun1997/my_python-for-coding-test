pos = input() # a1

x = int(pos[1])
y = ord(pos[0]) - ord('a') + 1

move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

count = 0
for i in range(8):
    nx = x + move[i][0]
    ny = y + move[i][1]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)