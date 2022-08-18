n = int(input())

info = []
for _ in range(n):
    name, d, m, y = map(str, input().split())
    info.append((name, int(d), int(m), int(y)))

info.sort(key=lambda x : (x[3], x[2], x[1]))

print(info[n-1][0])
print(info[0][0])