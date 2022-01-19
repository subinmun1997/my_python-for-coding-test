import sys
input = sys.stdin.readline

n = int(input())
cw = list(map(int, input().split()))
m = int(input())
bw = list(map(int, input().split()))

cw.sort(reverse=True)
bw.sort(reverse=True)

if max(cw) < max(bw):
    print(-1)

answer = 0
while len(bw) > 0:
    answer += 1
    for i in cw:
        for j in range(len(bw)):
            if i >= bw[j]:
                del bw[j]
                break

print(answer)


