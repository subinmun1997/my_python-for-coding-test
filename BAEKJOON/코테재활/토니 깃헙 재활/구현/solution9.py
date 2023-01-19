n = int(input())

cow = dict()
count = 0

for _ in range(n):
    x, y = map(int, input().split())
    if x not in cow:
        cow[x] = y
    else:
        if y != cow[x]:
            count += 1
            cow[x] = y

print(count)