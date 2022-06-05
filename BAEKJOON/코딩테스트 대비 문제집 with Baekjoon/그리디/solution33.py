t = int(input())
for _ in range(t):
    j, n = map(int, input().split())
    box = []
    for _ in range(n):
        r, c = map(int, input().split())
        box.append(r*c)
        box.sort(reverse=True)

    answer = 0
    for b in box:
        if j <= 0:
            break
        j -= b
        answer += 1

    print(answer)