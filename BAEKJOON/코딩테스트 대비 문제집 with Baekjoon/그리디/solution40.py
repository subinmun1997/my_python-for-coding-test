t = int(input())
for _ in range(t):
    n = int(input())
    before = input()
    after = input()

    count_w = 0
    count_b = 0

    for i in range(n):
        if before[i] != after[i]:
            if before[i] == 'W':
                count_w += 1
            else:
                count_b += 1

    print(max(count_b, count_w))