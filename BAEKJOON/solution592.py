t = int(input())
for _ in range(t):
    n = int(input()) #사다리 세로줄
    ladder = list(map(int, input().split()))
    sort_ladder = sorted(ladder)

    count = 0
    while ladder != sort_ladder:
        for i in range(n-1):
            if ladder[i] > ladder[i+1]:
                ladder[i], ladder[i+1] = ladder[i+1], ladder[i]
                count += 1

    print(count)