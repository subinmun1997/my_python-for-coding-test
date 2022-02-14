mushroom = []

for _ in range(10):
    mushroom.append(int(input()))

max_value = 0
for m in mushroom:
    max_value += m
    if max_value >= 100:
        if max_value - 100 > 100 - (max_value - m):
            max_value -= m
        break

print(max_value)
