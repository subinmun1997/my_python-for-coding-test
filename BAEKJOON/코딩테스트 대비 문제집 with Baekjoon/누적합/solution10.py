n, k = map(int, input().split())
numbers = list(map(int, input().split()))

prefix_sum = sum(numbers[:k])
answer = [prefix_sum]

for i in range(n-k):
    prefix_sum = prefix_sum - numbers[i] + numbers[i+k]
    answer.append(prefix_sum)

print(max(answer))