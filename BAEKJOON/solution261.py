n, k = map(int, input().split())
data = list(map(int, input().split()))

count = 0
for i in range(len(data)):
    min_index = i
    flag = 0
    for j in range(i+1, len(data)):
        if data[min_index] > data[j]:
            min_index = j
            flag = 1
    if flag == 1:
        data[i], data[min_index] = data[min_index], data[i]
        count += 1
        if count == k:
            print(data[i], data[min_index])
        flag = 0

if count < k:
    print(-1)





