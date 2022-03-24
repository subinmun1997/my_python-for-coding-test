n, m, k = map(int, input().split()) # 배열 크기, 더해지는 횟수, 연속 몇번까지
numbers = sorted(list(map(int, input().split())), reverse=True)

first = numbers[0] # 가장 큰 수
second = numbers[1] # 두번째로 큰 수

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


