n = int(input())
score = list(map(int, input().split()))

result = 0
for i in score:
    result += i / max(score) * 100

print(result/n)