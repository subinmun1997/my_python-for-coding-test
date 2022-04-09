n, k = map(int, input().split())
coin_type = [int(input()) for _ in range(n)]
coin_type.sort(reverse=True)

result = 0
for coin in coin_type:
    if coin <= k:
        result += k // coin
        k %= coin

print(result)