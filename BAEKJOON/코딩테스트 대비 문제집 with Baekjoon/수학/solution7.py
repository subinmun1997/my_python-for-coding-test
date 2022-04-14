def check(num):
    count = 0
    if num == 1:
        return False
    for i in range(2, num+1):
        if num%i == 0:
            count += 1

    if count > 1:
        return False
    else:
        return True

m = int(input())
n = int(input())

data = []
for i in range(m, n+1):
    if check(i):
        data.append(i)

print(data)
if data:
    print(sum(data))
    print(min(data))
else:
    print(-1)