n, p = map(int, input().split())

melody = [[] for i in range(7)]
count = 0
for _ in range(n):
    i, p = map(int, input().split())
    if melody[i] == [] or melody[i][-1] < p:
        melody[i].append(p)
        count += 1
    else:
        while melody[i] != [] and melody[i][-1] > p:
            melody[i].pop()
            count += 1
        if melody[i] != [] and melody[i][-1] == p:
            continue
        melody[i].append(p)
        count += 1

print(count)