from itertools import product

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

for i in product(nums, repeat=m):
    print(*i)