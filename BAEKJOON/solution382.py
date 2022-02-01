temp = [i for i in range(1, 31)]

for _ in range(28):
    temp.remove(int(input()))

temp.sort()
for i in temp:
    print(i)