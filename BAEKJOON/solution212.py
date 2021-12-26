s = int(input())

temp = 1
ans = 0

while True:
    s -= temp
    if s >= 0:
        temp += 1
        ans += 1
    else:
        print(ans)
        break