n = int(input())
cand = {}

for _ in range(n):
    name = input()
    if name in cand:
        cand[name] += 1
    else:
        cand[name] = 1

for _ in range(n-1):
    name = input()
    cand[name] -= 1

for name, cnt in cand.items():
    if cnt != 0:
        print(name)