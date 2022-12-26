n, m, k = map(int, input().split())
num = sorted(list(map(int, input().split())), reverse=True)

first = num[0]
second = num[1]

result = 0
while True:
    for _ in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break
    result += second
    m -= 1

print(result)

