num = input().split('-')
data = []

for i in num:
    sep = i.split('+')
    temp = 0
    for j in sep:
        temp += int(j)
    data.append(temp)

result = data[0]
for i in range(1, len(data)):
    result -= data[i]

print(result)