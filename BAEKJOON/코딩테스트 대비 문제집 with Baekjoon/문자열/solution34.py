pikachu = ["pi", "ka", "chu"]
s = input()

for i in pikachu:
    if i in s:
        s = s.replace(i, "X")

cnt = 0
for i in s:
    if i != 'X':
        cnt += 1

print("YES" if not cnt else "NO")