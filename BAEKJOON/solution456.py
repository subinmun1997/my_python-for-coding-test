n = int(input())

count = 0
i = 1
while n != 0:
    if n >= i:
        count += 1
        n -= i
        i += 1
    else:
        i = 1

print(count)