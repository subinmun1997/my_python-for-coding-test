t = int(input())

for _ in range(t):
    box = []
    j, n = map(int, input().split())

    for _ in range(n):
        r, c = map(int, input().split())
        box.append(r*c)

    box.sort(reverse=True)

    count = 0
    for b in box:
        if j <= 0:
            break
        count += 1
        j -= b

    print(count)