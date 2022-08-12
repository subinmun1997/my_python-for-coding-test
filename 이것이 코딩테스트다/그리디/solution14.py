n, m, k = map(int, input().split())
num = sorted(list(map(int, input().split())), reverse=True)

first = num[0]
second = num[1]

count = (m // (k+1)) * k + (m % (k+1))
result = count * first
result += (m - count) * second

print(result)