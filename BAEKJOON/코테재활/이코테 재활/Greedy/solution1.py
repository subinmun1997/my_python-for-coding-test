n = int(input())

coins = [500, 100, 50, 10]
count = 0
for coin in coins:
    count += n // coin # 큰 값부터 최대한으로 나누는 것이 최소 값 구할 수 있는 방법
    n %= coin

print(count)