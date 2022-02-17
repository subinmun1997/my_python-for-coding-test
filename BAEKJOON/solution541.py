n = int(input())
pps = [list(map(str, input().split())) for _ in range(n)]
cseteram = list(map(str, input().split()))

for item in cseteram:
    flag = False
    for idx in range(n):
        if pps[idx] and item == pps[idx][0]:
            pps[idx].pop(0)
            flag = True
            break
    if not flag:
        break

left = 0
for line in pps:
    left += len(line)

if flag and left == 0:
    print("Possible")
else:
    print("Impossible")