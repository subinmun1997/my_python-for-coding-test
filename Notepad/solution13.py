pos = input()
row = int(pos[1]) #행
col = int(ord(pos[0])) - int(ord('a')) + 1 #열

move_type = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

answer = 0
for r, c in move_type:
    nrow = row + r
    ncol = col + c

    if nrow >= 1 and nrow <= 8 and ncol >= 1 and ncol <= 8:
        answer += 1

print(answer)
