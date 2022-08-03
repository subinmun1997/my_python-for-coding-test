n = int(input())
km = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
curPrice = price[0]
for i in range(len(km)):
    result += curPrice * km[i]
    if curPrice > price[i+1]:
        curPrice = price[i+1]

print(result)