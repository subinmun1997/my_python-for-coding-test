n = int(input())
l = list(map(int, input().split()))
m = list(map(int, input().split()))

result = 0
start = m[0]

for i in range(len(l)):
    if m[i] < start:
        start = m[i]
    result += start * l[i]

print(result)