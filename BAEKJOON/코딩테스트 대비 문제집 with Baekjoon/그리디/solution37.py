t = int(input())
for _ in range(t):
    n, m = map(str, input().split())
    diff0 = 0
    diff1 = 0

    for i in range(len(n)):
        if n[i] != m[i]:
            if n[i] == '1':
                diff1 += 1
            else:
                diff0 += 1

    answer = 0
    while diff0 > 0 and diff1 > 0:
        answer += 1
        diff0 -= 1
        diff1 -= 1

    answer += (diff0 + diff1)
    print(answer)