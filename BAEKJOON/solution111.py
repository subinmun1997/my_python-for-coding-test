array = []

max_number = []
for i in range(4):
    array.append(list(map(int, input().split())))

count = 0
for i,j in array:
    count -= i
    count += j
    max_number.append(count)

print(max(max_number))
