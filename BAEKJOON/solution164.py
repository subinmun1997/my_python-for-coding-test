date = int(input())
car = list(map(int, input().split()))

cnt = 0

for i in car:
    if i == date:
        cnt += 1

print(cnt)