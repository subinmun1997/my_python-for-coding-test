n, k = map(int, input().split()) # 원생 수, 조의 개수
height = list(map(int, input().split()))

diff = []
for i in range(n-1):
    diff.append(height[i+1]-height[i]) # 원생 들의 키 차이

diff.sort()

cost = 0
for i in range(n-k):
    cost += diff[i]

print(cost)