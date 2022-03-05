n = int(input())
tip = [int(input()) for _ in range(n)]
tip.sort(reverse=True)

total_tip = 0
for i in range(n):
    temp = tip[i] - i
    if temp > 0:
        total_tip += temp

print(total_tip)