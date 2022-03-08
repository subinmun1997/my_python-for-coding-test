n = int(input())
milk = [int(input()) for _ in range(n)]
milk.sort(reverse=True)

answer = 0
for i in range(0, n, 3):
    temp = milk[i:i+3]
    if len(temp) < 3:
        answer += sum(temp)
    else:
        answer += sum(temp[:2])

print(answer)