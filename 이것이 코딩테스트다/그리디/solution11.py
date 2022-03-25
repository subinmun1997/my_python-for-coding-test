n, m = map(int, input().split()) # 볼링공의 개수, 공의 최대 무게
weight = list(map(int, input().split()))

answer = 0
for i in range(n-1):
    for j in range(i+1, n):
        if weight[i] != weight[j]:
            answer += 1

print(answer)
