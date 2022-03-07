numbers = [0] * 500001
n = int(input())
array = list(map(int, input().split()))

for a in array:
    numbers[a] += 1

print(max(numbers))