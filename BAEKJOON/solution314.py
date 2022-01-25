a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a*1000)
elif a == b or a == c:
    print(1000 + a*100)
elif b == c:
    print(1000 + b*100)
else:
    max_value = max(a,b,c)
    print(max_value*100)
