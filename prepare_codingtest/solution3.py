n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)

first = data[0]
second = data[1]

count = (m // (k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)