t = int(input())
for _ in range(t):
    n, m = map(str, input().split())

    count0 = 0
    count1 = 0
    for i in range(len(n)):
        if n[i] != m[i]:
            if n[i] == '0':
                count1 += 1
            else:
                count0 += 1

    print(max(count0, count1))