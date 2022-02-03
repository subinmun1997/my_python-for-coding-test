t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    one_leg = m * 2 - n
    print(one_leg, m - one_leg)
