target = int(input())
answer = abs(100 - target)
m = int(input())
if m:
    broken = list(map(str, input().split()))
else:
    broken = list()

for num in range(1000001):
    for n in str(num):
        if n in broken:
            break
    else:
        answer = min(answer, len(str(num)) + abs(num - target))

print(answer)
