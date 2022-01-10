n = int(input())

data = list(set(map(int, input().split())))

data.sort()

for i in data:
    print(i, end=' ')