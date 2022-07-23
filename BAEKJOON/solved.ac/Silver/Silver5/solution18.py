n = int(input())

info = []
for i in range(n):
    age, name = map(str, input().split())
    info.append((int(age), name, i))

info.sort(key=lambda x : (x[0], x[2]))
for i in info:
    print(i[0], i[1])