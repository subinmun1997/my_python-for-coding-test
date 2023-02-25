n, m = map(int, input().split())

result = 0
for _ in range(n):
    nums = list(map(int, input().split()))
    temp = min(nums) # 현재 줄에서 가장 작은 수 찾기
    result = max(result, temp) # 가장 작은 수들 중에서 가장 큰 수 찾기

print(result)