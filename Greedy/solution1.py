data = int(input())
coins = [500, 100, 50, 10]
cnt = 0

for coin in coins:
    cnt += data // coin
    data %= coin

print(cnt)