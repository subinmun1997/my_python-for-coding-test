def junhyeon(money, stock):
    jMoney = money
    jStock = 0

    for i in stock:
        if jMoney >= i:
            newStock = jMoney // i
            jStock += newStock
            jMoney -= i * newStock

    jResult = jMoney + (stock[-1] * jStock)
    return jResult

def sungmin(money, stock):
    sMoney = money
    sStock = 0

    for i in range(3, len(stock)):
        if stock[i-3] < stock[i-2] < stock[i-1] < stock[i] and sStock != 0:
            sMoney += sStock * stock[i]
            sStock = 0
        elif stock[i] < stock[i-1] < stock[i-2] < stock[i-3]:
            new_stock = sMoney // stock[i]
            sStock += new_stock
            sMoney -= stock[i] * new_stock

    sResult = sMoney + (stock[-1] * sStock)
    return sResult

money = int(input())
stock = list(map(int, input().split()))

if junhyeon(money, stock) > sungmin(money, stock):
    print("BNP")
elif junhyeon(money, stock) < sungmin(money, stock):
    print("TIMING")
else:
    print("SAMESAME")