n = int(input())
data = sorted(list(map(int, input().split())))

result = []
if n%2 == 0:
    for i in range(len(data) // 2):
        result.append(data[i] + data[n - 1 - i])
else:
    result.append(data.pop())
    for i in range(len(data) // 2):
        result.append(data[i] + data[n - 2 - i])

print(max(result))
