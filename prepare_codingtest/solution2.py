n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))
data.sort(reverse=True)

first = data[0]
second = data[1]
value = 0

while True:
    for i in range(k):
        if m == 0:
            break
        value += first
        m -= 1
    if m == 0:
        break
    value += second
    m -= 1

print(value)

print(value)