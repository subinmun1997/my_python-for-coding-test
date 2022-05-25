n = int(input())
numbers = list(map(int, input().split()))

result = [numbers[0]]
for i in range(n-1):
    result.append(max(result[i]+numbers[i+1], numbers[i+1]))

print(max(result))