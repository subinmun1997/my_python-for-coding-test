def junhyeon(stock, money):
    jstock = 0
    jmoney = money
    for i in stock:
        if jmoney >= i:
            jstock += jmoney // i
            jmoney -= i * jstock

    jresult = jmoney + (stock[-1] * jstock)
    return jresult

def sungmin(stock, money):
    sstock = 0
    smoney = money
    for i in range(3, len(stock)):
        if stock[i-3] < stock[i-2] < stock[i-1] < stock[i] and sstock != 0:
            smoney += sstock * stock[i]
            sstock = 0
        elif stock[i-3] > stock[i-2] > stock[i-1] > stock[i] and smoney >= stock[i]:
            sstock += smoney // stock[i]
            smoney -= sstock * stock[i]

    sresult = smoney + stock[-1] * sstock
    return sresult

money = int(input())
stock = list(map(int, input().split()))
if junhyeon(stock, money) > sungmin(stock, money):
    print("BNP")
elif junhyeon(stock, money) < sungmin(stock, money):
    print("TIMING")
else:
    print('SAMESAME')