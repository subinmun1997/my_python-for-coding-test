a, b = map(int, input().split())

cnt = 1
while True:
    if a == b:
        break
    elif a>b or (b%10 != 1 and b%2 != 0):
        cnt = -1
        break
    elif b%10 == 1:
        b //= 10
        cnt += 1
    elif b%2 == 0:
        b //= 2
        cnt += 1

print(cnt)
