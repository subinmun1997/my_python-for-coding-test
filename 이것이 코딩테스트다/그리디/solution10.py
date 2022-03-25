n = int(input())
coins = sorted(list(map(int, input().split())))

max_coin = 1
for coin in coins:
    if max_coin < coin: # 만들 수 없는 금액을 찾았을 때 반복 종료
        break
    max_coin += coin

print(max_coin)