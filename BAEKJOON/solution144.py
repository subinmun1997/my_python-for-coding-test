n, c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

gap = (data[-1] - data[0]) // (c-1)

while True:
    x = 0
    count = 1
    for i in range(1, n):
        if data[i] - data[x] >= gap:
            count += 1
            x = i

    if count >= c:
        break
    else:
        gap -= 1

print(gap)
