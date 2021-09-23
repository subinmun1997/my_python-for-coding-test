n = int(input())

coin_type = [500, 100, 50, 10, 5, 1]
change = 1000 - n

result = 0
for coin in coin_type:
    result += change // coin
    change %= coin

print(result)