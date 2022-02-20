n, k = map(int, input().split())
female = [0] * 1000
male = [0] * 1000

for _ in range(n):
    s, y = map(int, input().split())
    if s == 0:
        female[y] += 1
    else:
        male[y] += 1

room = 0
for i in range(1, 7):
    if female[i] % k == 0:
        room += female[i] // k
    else:
        room += female[i] // k + 1

    if male[i] % k == 0:
        room += male[i] // k
    else:
        room += male[i] // k + 1

print(room)
