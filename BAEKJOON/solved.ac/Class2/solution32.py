n = int(input())

info = []
for i in range(n):
    age, name = input().split()
    info.append((int(age), name, i))

info.sort(key=lambda x : (x[0], x[2]))
for age, name, idx in info:
    print(age, name)

