data = input().split('-')
num = []

for i in data:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)

first = num[0]
for i in range(1, len(num)):
    first -= num[i]

print(first)
