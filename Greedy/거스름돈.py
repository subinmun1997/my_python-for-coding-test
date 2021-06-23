n = int(input())

coin_types = [500,100,50,10]
count = 0

for coin in coin_types:
    count += n // coin
    n = n % coin

print(count)