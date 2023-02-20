from itertools import combinations

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

comb = set(combinations(nums, m))
for i in sorted(comb):
    print(*i)