data = [int(input()) for _ in range(5)]

total = 0
for i in data:
    if i >= 40:
        total += i
    else:
        total += 40

print(total//5)