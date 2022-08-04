n = int(input())

exist = []
for _ in range(n):
    name, log = input().split()

    if log == "enter":
        exist.append(name)
    elif log == "leave":
        exist.pop(exist.index(name))

exist.sort(reverse=True)
for i in exist:
    print(i)