n, a, d = map(int, input().split())
melody = list(map(int, input().split()))

answer = 0
x = 0
for i in range(n):
    if melody[i] == a+(d*x):
        answer += 1
        x += 1

print(answer)