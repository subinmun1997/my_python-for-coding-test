r, c = map(int, input().split())
row = [0, r]
col = [0, c]

for _ in range(int(input())):
    rc, line = map(int, input().split())
    if rc == 1:
        row.append(line)
    else:
        col.append(line)

row.sort()
col.sort()

sub_row = []
sub_col = []

for i in range(len(row) - 1):
    sub_row.append(row[i+1] - row[i])
for i in range(len(col) - 1):
    sub_col.append(col[i+1] - col[i])

print(max(sub_col) * max(sub_row))

