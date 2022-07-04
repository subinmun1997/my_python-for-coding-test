n, m, k = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())), reverse=True)

first = arr[0]
second = arr[1]

answer = 0
while True:
    for i in range(k):
        if m == 0:
            break
        answer += first
        m -= 1
    if m == 0:
        break
    answer += second
    m -= 1

print(answer)
