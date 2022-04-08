array = []
for _ in range(5):
    array.append(input())

for i in range(max([len(e) for e in array])):
    for j in range(5):
        if len(array[j]) > i:
            print(array[j][i], end='')
