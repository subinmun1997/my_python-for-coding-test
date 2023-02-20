from itertools import permutations

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

for i in permutations(nums, m):
    print(*i)