n = input()
row = int(n[1])
col = int(ord(n[0])) - int(ord('a')) + 1

move_type = [(-2,1),(-2,-1),(2,1),(2,-1),(-1,2),(-1,-2),(1,-2),(1,2)]

answer = 0
for x, y in move_type:
    nrow = row + x
    ncol = col + y

    if nrow >= 1 and nrow <= 8 and ncol >= 1 and ncol <= 8:
        answer += 1

print(answer)