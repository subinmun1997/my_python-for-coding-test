d = [0] * 1001
n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    d[a] = b

for i in range(d.index(max(d))):
    if d[i] > d[i + 1]:
        d[i+1] = d[i]

for j in range(1000, d.index(max(d)), -1):
    if d[j] > d[j-1]:
        d[j-1] = d[j]

print(sum(d))