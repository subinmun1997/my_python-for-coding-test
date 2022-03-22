n, m = map(int, input().split())
location = list(map(int, input().split()))

positive = [i for i in location if i > 0] # 양수
negative = [i for i in location if i < 0] # 음수

max_value = 0
for loc in location:
    if abs(loc) > abs(max_value):
        max_value = loc
answer = 0

positive.sort(reverse=True)
negative.sort()

distance = []
for i in range(0, len(positive), m):
    if positive[i] != max_value:
        distance.append(positive[i])

for i in range(0, len(negative), m):
    if negative[i] != max_value:
        distance.append(negative[i])

answer = abs(max_value)
for i in distance:
    answer += abs(i*2)

print(answer)


