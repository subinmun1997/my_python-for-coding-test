n = int(input())
product = list(map(int, input().split()))

m = int(input())
request = list(map(int, input().split()))

count_array = [0] * 1000001
for i in product:
    count_array[i] += 1

for i in request:
    if count_array[i] != 0:
        print("yes", end=' ')
    else:
        print("no", end=' ')