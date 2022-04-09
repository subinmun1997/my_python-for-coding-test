n = int(input())
price = [int(input()) for _ in range(n)]

price.sort(reverse=True)

result = 0
for i in range(0, n, 3):
    temp = price[i:i+3]
    if len(temp) < 3:
        result += sum(temp)
    else:
        result += sum(temp[:2])

print(result)