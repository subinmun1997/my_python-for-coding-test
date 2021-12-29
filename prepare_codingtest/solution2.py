n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))
data.sort(reverse=True)

first = data[0]
second = data[1]
value = 0

while True:
    if m == 0:
        break
    else:
        for i in range(k):
            value += first
            m -= 1
        value += second
        m -= 1

print(value)