import sys
k, n = map(int, sys.stdin.readline().split())
lan = []
for i in range(k):
    lan.append(int(sys.stdin.readline()))
lan.sort()

start = 1
end = max(lan)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in lan:
        total += (i // mid)

    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)