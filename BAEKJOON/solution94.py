n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

for i in array:
    rank = 1
    for j in array:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    print(rank , end=' ')