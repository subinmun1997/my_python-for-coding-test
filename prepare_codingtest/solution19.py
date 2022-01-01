n = input()
row = int(n[1])
col = int(ord(n[0])) - int(ord('a')) + 1

move_type = [(-2,1),(-2,-1),(2,1),(2,-1),(-1,2),(1,2),(-1,-2),(1,-2)]

result = 0

for i in move_type:
    nrow = row + i[1]
    ncol = col + i[0]

    if nrow < 1 or nrow > 8 or ncol < 1 or ncol > 8:
        continue
    result += 1

print(result)