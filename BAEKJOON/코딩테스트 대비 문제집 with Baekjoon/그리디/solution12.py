n = int(input())
data = list(input())
data.append('A')

result = [1] * 2

for i in range(n):
    if data[i] == 'B':
        continue
    elif data[i] == 'R':
        result[0] += 1
        if data[i+1] == 'R':
            result[0] -= 1
            continue

for i in range(n):
    if data[i] == 'R':
        continue
    elif data[i] == 'B':
        result[1] += 1
        if data[i+1] == 'B':
            result[1] -= 1
            continue

print(min(result))