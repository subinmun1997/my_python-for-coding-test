n = int(input())

numbers = list(map(int, input().split()))
result = []
result.append(numbers[0])

for i in range(1, n):
    result.append(result[i-1] + numbers[i])

answer = 0
for i in range(n):
    answer += numbers[i] * (result[n-1] - result[i])

print(answer)