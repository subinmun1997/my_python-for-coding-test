x, y = map(int, input().split())

array = []
num = 1
while len(array) <= 1000:
    for i in range(num):
        array.append(num)
    num += 1

print(sum(array[x-1:y]))