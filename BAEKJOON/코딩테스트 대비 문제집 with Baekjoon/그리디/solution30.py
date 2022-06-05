n, w = map(int, input().split())
bytecoin = [int(input()) for _ in range(n)]

coin = 0
for i in range(n-1):
    if bytecoin[i] < bytecoin[i+1]: # 매수
        if w >= bytecoin[i]:
            coin += w // bytecoin[i]
            w -= bytecoin[i] * coin
    elif bytecoin[i] > bytecoin[i-1]: # 매도
        w += coin * bytecoin[i]
        coin = 0

if coin > 0:
    w += coin * bytecoin[-1]

print(w)
