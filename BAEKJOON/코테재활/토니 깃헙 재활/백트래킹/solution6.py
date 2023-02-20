from itertools import product

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

for i in product(nums, repeat=m):
    print(*i)