data = list(map(int, input().split()))

result = 0
for i in data:
    result += i*i

print(result%10)