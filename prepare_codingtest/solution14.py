n = int(input())
coins = list(map(int, input().split()))
coins.sort()

result = 1
for coin in coins:
    if result >= coin:
        result += coin
    else:
        break

print(result)
