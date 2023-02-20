from itertools import combinations

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

for i in combinations(nums, m):
    print(*i)