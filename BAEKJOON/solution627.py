h, w = map(int, input().split())
block = list(map(int, input().split()))

array = []
start = block[0]
flag = False
temp = []
for i in range(1, w):
    if flag:
        start = block[i]
        temp = []
        flag = False
    if block[i] >= start:
        temp.append(block[i])
        array.append(temp)
        temp = []
        flag = True
    else:
        temp.append(block[i])

array.append(temp)
print(array)

