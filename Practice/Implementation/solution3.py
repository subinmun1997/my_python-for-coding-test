n = input()
row = int(n[1])
column = int(ord(n[0])) - int(ord('a')) + 1 # ord(변수) : 아스키 코드로 변환하는 함수
move_types= [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,2),(1,-2)]

count = 0
for r,c in move_types:
    nrow = row + r
    ncol = column + c

    if nrow >= 1 and nrow <= 8 and ncol >=1 and ncol <= 8:
        count += 1

print(count)
