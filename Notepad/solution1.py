n = int(input())
coins = [500, 100, 50, 10]

answer = 0
for coin in coins:
    answer += n // coin
    n %= coin

print(answer)