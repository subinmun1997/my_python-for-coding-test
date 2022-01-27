n = int(input())

money = []
for _ in range(n):
    result = 0
    a, b, c = map(int, input().split())
    if a == b == c:
        result = 10000 + a*1000
    elif a == b or a == c:
        result = 1000 + a*100
    elif b == c:
        result = 1000 + b*100
    else:
        result = max(a,b,c) * 100
    money.append(result)

print(max(money))