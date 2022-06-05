n, w = map(int, input().split())
price = [int(input()) for _ in range(n)]

coin = 0
for i in range(n-1):
    if i == 0:
        if price[i] < price[i+1]:
            coin += w // price[i]
            w -= price[i] * coin
    else:
        if price[i-1] >= price[i] and price[i] < price[i+1]: # 매수
            if w >= price[i]:
                coin += w // price[i]
                w -= price[i] * coin
        if price[i-1] <= price[i] and price[i] > price[i+1]: # 매도
            if coin:
                w += price[i] * coin
                coin -= w // price[i]

w += price[-1] * coin
print(w)
