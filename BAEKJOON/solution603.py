def jun(seed, stock):
    buy_stock = 0 # 보유 주식 수
    has_money = seed # 남은 현금
    for i in range(len(stock)-1):
        if has_money >= stock[i]:
            buy_stock += has_money // stock[i]
            has_money -= buy_stock * stock[i]

    has_money += stock[-1] * buy_stock
    return has_money

def sung(seed, stock):
    buy_stock = 0 # 보유 주식 수
    has_money = seed # 남은 현금
    for i in range(3, len(stock)):
        if stock[i-3] < stock[i-2] < stock[i-1] < stock[i] and buy_stock != 0:
            has_money += buy_stock * stock[i]
            buy_stock = 0
        elif stock[i-3] > stock[i-2] > stock[i-1] > stock[i] and has_money >= stock[i]:
            buy_stock += has_money // stock[i]
            has_money -= buy_stock * stock[i]

    has_money += stock[-1] * buy_stock
    return has_money

seed = int(input())
stock = list(map(int, input().split()))
if jun(seed, stock) > sung(seed, stock):
    print("BNP")
elif jun(seed, stock) < sung(seed, stock):
    print('TIMING')
else:
    print("SAMESAME")