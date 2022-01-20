n = int(input())

arr = [[0 for _ in range(101)] for _ in range(101)]

for i in range(n):
    a, b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1

count = 0
for i in arr:
    count += i.count(1)

print(count)
