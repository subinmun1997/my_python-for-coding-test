import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleep_student = list(map(int, input().split()))
attend_student = list(map(int, input().split()))

sleep = [0] * (n+3)
check = [0] * (n+3)

for i in sleep_student:
    sleep[i] = 1
for i in attend_student:
    if sleep[i]:
        continue
    for j in range(i, n+3, i):
        if not sleep[j]:
            check[j] = 1

prefix = [check[0]]
for i in range(1, n+3):
    prefix.append(prefix[-1] + check[i])

for _ in range(m):
    s, e = map(int, input().split())
    print(e-s+1 - (prefix[e] - prefix[s-1]))

