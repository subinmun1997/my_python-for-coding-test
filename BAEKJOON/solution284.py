m = int(input())
n = int(input())

numbers = []
for i in range(m, n+1):
    tmp = int(i ** 0.5)
    if tmp * tmp == i:
        numbers.append(i)
if numbers:
    print(sum(numbers))
    print(min(numbers))
else:
    print(-1)