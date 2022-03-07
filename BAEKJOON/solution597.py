t = int(input())

for _ in range(t):
    n = int(input())
    before = list(map(str, input()))
    after = list(map(str, input()))
    w_cnt = 0
    b_cnt = 0
    for i in range(n):
        if before[i] == 'W' and after[i] == 'B':
            b_cnt += 1
        elif before[i] == 'B' and after[i] == 'W':
            w_cnt += 1

    print(max(b_cnt, w_cnt))