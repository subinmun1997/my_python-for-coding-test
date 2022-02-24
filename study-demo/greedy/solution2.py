n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

first = numbers[n-1]
second = numbers[n-2]

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