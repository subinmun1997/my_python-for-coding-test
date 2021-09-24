n = int(input())

data = [int(input()) for _ in range(n)]
data.sort()

for i in data:
    print(i)