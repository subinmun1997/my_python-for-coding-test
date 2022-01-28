n = int(input())
answer = 0

for i in range(n+1):
    for j in range(i, n+1):
        answer += (i+j)

print(answer)