count = 0

n = int(input())
for i in range(n+1, n**2, n+1):
    count += i

print(count)