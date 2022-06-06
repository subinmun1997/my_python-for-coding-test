n, m = map(int, input().split())
if n == 0:
    print(0)
    exit()

w = list(map(int, input().split()))
answer = 1
temp = 0
for i in w:
    temp += i
    if temp > m:
        answer += 1
        temp = i

print(answer)