n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

counting_sort = [0] * (max(array)+1)

for i in array:
    counting_sort[i] += 1

for i in range(len(counting_sort)):
    for j in range(counting_sort[i]):
        print(i)