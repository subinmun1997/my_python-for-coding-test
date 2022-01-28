numbers = []

for _ in range(5):
    numbers.append(int(input()))

numbers.sort()
print(sum(numbers)//5)
print(numbers[2])