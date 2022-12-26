n, m, k = map(int, input().split())
num = sorted(list(map(int, input().split())), reverse=True)

first = num[0]
second = num[1]

temp = (m // (k+1) * k) + (m % (k+1))
result = (temp * first) + (m - temp) * second

print(result)