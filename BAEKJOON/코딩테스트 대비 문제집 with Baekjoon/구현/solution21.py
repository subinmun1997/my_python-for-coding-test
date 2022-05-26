n = int(input())
numbers = [i for i in range(1, n+1)]
temp = []

while len(numbers) != 1:
    for idx, item in enumerate(numbers):
        if idx%2 != 0:
            temp.append(item)
    numbers = temp
    temp = []

print(numbers[0])
