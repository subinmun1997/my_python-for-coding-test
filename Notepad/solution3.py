n, m, k = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)

first = arr[0]
second = arr[1]

# 가장 큰 수가 더해지는 횟수
count = int(m / (k+1)) * k
count += m % (k+1)

answer = 0
answer += first * count
answer += (m-count) * second

print(answer)