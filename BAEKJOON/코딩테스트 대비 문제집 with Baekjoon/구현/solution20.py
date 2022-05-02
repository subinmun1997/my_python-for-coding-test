import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trains = [set([]) for _ in range(n)]

for _ in range(m):
    op = list(map(int, input().split()))
    if op[0] == 1:
        trains[op[1]-1].add(op[2])
    elif op[0] == 2:
        trains[op[1]-1].discard(op[2])
    elif op[0] == 3:
        tr = list(trains[op[1]-1])
        temp = set()
        for t in tr:
            if t+1 > 20:
                continue
            temp.add(t+1)
        trains[op[1]-1] = temp
    elif op[0] == 4:
        tr = list(trains[op[1]-1])
        temp = set()
        for t in tr:
            if t-1 < 1:
                continue
            temp.add(t-1)
        trains[op[1]-1] = temp

answer = set()
for train in trains:
    t = tuple(sorted(train))
    answer.add(t)
print(len(answer))

