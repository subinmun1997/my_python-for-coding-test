data = input().split('-')

result = []
for i in data:
    temp = i.split('+')
    cnt = 0
    for i in temp:
        cnt += int(i)
    result.append(cnt)

answer = result[0]
for i in range(1, len(result)):
    answer -= result[i]

print(answer)

