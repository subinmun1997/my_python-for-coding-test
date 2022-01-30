people = []

for _ in range(10):
    x, y = map(int, input().split()) # x:내린 사람, y:탄 사람
    people.append((x, y))

total = []
temp = 0
for x, y in people:
    temp -= x
    temp += y
    total.append(temp)

print(max(total))
