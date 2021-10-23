n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

first = data[n-1]
second = data[n-2]

count = 0
while True:
    if m == 0:
        break
    else:
        for i in range(k):
            count += first
            m -= 1
        if m == 0:
            break
        else:
            count += second
            m -= 1

print(count)