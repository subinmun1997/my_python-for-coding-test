import itertools
n, m = map(int, input().split())

nums = list(map(int, input().split()))
data = itertools.combinations(nums, 3)

data2 = []
for i in data:
    if sum(i) <= m:
        data2.append(i)

total = []
for i in data2:
    total.append(sum(i))

print(max(total))
