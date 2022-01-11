import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

count = 0
for i in range(n-1,0,-1):
    flag = 0
    max_idx = i
    for j in range(i-1,-1,-1):
        if data[max_idx] < data[j]:
            max_idx = j
            flag = 1
    if flag == 1:
        data[i], data[max_idx] = data[max_idx], data[i]
        count += 1
        flag = 0
        if count == k:
            print(data[max_idx],data[i])

if count < k:
    print(-1)

