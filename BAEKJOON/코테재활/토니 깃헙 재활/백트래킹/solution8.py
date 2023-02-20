from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

for i in combinations_with_replacement(nums, m):
    print(*i)