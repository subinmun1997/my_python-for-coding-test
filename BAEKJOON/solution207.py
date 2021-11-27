array = []
for _ in range(10):
    array.append(int(input()))

total = 0
for i in range(1,10):
    total += array[i]

print(array[0] - total)