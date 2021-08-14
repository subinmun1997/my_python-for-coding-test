n, m, k = map(int, input().split())

data = input().split()
data.sort(reverse=True)

res = 0
first = int(data[0])
second = int(data[1])

while True:
    for i in range(k):
        if m == 0:
            break
        else:
            res += first
            m -= 1
    if m == 0:
        break
    else:
        res += second
        m -= 1

print(res)