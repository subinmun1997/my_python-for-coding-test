a = int(input())
b = int(input())
c = int(input())
numbers = [0] * 10
mul = str(a*b*c)

for m in mul:
    numbers[int(m)] += 1

for i in range(10):
    print(numbers[i])