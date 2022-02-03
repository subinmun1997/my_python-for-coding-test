t = int(input())
for _ in range(t):
    n = int(input())
    profit = 0
    for _ in range(n):
        data = list(map(int, input().split()))
        max_data = max(data)
        if max_data >= 0:
            profit += max_data
    print(profit)