n = int(input())
milk = list(map(int, input().split()))
check = 0 # 우유 마시는 순서

count = 0
for m in milk:
    if m == check:
        count += 1
        check += 1
    if check == 3:
        check = 0

print(count)