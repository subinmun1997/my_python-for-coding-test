n = int(input())
numbers = list(map(int, input().split()))

result = []
if n == 2:
    for i in range(1, min(numbers)+1):
        if numbers[0] % i == 0 and numbers[1] % i == 0:
            result.append(i)
    for j in result:
        print(j)

elif n == 3:
    for i in range(1, min(numbers)+1):
        if numbers[0] % i == 0 and numbers[1] % i == 0  and numbers[2] % i == 0:
            result.append(i)
    for j in result:
        print(j)