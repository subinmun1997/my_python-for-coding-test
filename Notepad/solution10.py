n, m = map(int, input().split())
k = list(map(int, input().split()))

answer = 0
for i in range(n-1):
    for j in range(i+1, n):
        if k[i] != k[j]:
            answer += 1

print(answer)