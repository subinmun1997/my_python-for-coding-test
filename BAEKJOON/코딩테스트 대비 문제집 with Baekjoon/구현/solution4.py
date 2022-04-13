n, m = map(int, input().split())
s = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(m)]

for i in data:
    if i[0] == 1:
        s[i[1]-1] = i[2]
    elif i[0] == 2:
        for i in range(i[1]-1, i[2]):
            if s[i] == 1:
                s[i] = 0
            else:
                s[i] = 1
    elif i[0] == 3:
        for i in range(i[1]-1, i[2]):
            if s[i] == 1:
                s[i] = 0
    else:
        for i in range(i[1]-1, i[2]):
            if s[i] == 0:
                s[i] = 1

print(*s)