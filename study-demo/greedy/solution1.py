n = int(input()) # 손님에게 거슬러 줘야 할 돈
coins = [500, 100, 50, 10]
answer = 0 # 거슬러 줘야 할 동전의 개수

for coin in coins:
    answer += n // coin
    n %= coin

print(answer)