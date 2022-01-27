n = int(input())

dots = []
for _ in range(n):
    a, b = map(int, input().split())
    dots.append((a, b))

Q1 = Q2 = Q3 = Q4 = AXIS = 0
for x, y in dots:
    if x == 0 or y == 0:
        AXIS += 1
    elif x > 0 and y > 0:
        Q1 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    else:
        Q4 += 1

print("Q1:",Q1)
print("Q2:",Q2)
print("Q3:",Q3)
print("Q4:",Q4)
print("AXIS:",AXIS)