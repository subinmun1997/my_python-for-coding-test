from itertools import permutations

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = set(permutations(nums, m))
for i in sorted(result):
    print(*i)