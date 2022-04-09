n = int(input())
data = sorted(list(map(int, input().split())))

result = []
if n%2 != 0:
    result.append(data.pop())

for i in range(n//2):
    result.append(data[i] + data[len(data)-1-i])

print(max(result))