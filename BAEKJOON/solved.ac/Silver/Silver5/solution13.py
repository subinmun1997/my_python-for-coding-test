n = int(input())
info = []

for _ in range(n):
    y, x = map(int, input().split())
    info.append((x, y))

for h, w in info:
    score = 1
    for th, tw in info:
        if h < th and w < tw:
            score += 1
    print(score, end=' ')
