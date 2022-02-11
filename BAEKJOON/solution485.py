n = int(input())
numbers_B = list(map(int, input().split()))
numbers_A = []

for i in range(n):
    if i == 0:
        x = numbers_B[i] * (i+1)
        numbers_A.append(x)
    else:
        x = numbers_B[i] * (i+1) - sum(numbers_A)
        numbers_A.append(x)

for a in numbers_A:
    print(a, end=' ')