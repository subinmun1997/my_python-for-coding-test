n = int(input())
tip = [int(input()) for _ in range(n)]
tip.sort(reverse=True)

result = 0
for i in range(n):
    temp = tip[i] - i
    if temp > 0:
        result += temp

print(result)