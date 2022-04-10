n = int(input())
data = list(input())
data.append('A')

count = [1] * 2

for i in range(n): # 파란색으로 칠하는 경우
    if data[i] == 'B':
        continue
    elif data[i] == 'R':
        count[0] += 1
        if data[i+1] == 'R':
            count[0] -= 1
            continue

for i in range(n): # 빨간색으로 칠하는 경우
    if data[i] == 'R':
        continue
    elif data[i] == 'B':
        count[1] += 1
        if data[i+1] == 'B':
            count[1] -= 1
            continue

print(min(count))