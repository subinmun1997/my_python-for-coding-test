n = int(input())
guitar = []

for _ in range(n):
    num = 0
    serial = input()
    for s in serial:
        if s.isdigit():
            num += int(s)

    guitar.append((serial, num))

guitar.sort(key=lambda x : (len(x[0]), x[1], x[0]))

for g in guitar:
    print(g[0])