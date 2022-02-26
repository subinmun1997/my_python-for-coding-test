n = int(input())
coin = sorted(list(map(int, input().split())))

target = 1
for x in coin:
    if target < x:
        break
    target += x

print(target)