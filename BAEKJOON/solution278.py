n = int(input())
m = list(map(int, input().split()))

cnt = []
for i in range(n-1):
    tmp = 0
    for j in range(i+1, n):
        if m[i] >= m[j]:
            tmp += 1
        else:
            break
    cnt.append(tmp)

print(max(cnt))