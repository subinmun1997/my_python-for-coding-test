import math

total = 0
n = input()
for i in n:
    total += math.pow(int(i), 5)

print(f"{total:.0f}")