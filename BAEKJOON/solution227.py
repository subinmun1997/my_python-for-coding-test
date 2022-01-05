t = int(input())

coins = [25, 10, 5, 1]

for i in range(t):
    c = int(input())
    for coin in coins:
        if coin == 1:
            print(c//coin)
        else:
            print(c//coin, end=' ')
            c %= coin
print()

