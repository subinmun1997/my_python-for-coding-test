n = int(input())
stick = list(map(int, input().split()))
value = sum(stick)

answer = 0
for i in range(n):
    value -= stick[i]
    answer += stick[i] * value

print(answer)