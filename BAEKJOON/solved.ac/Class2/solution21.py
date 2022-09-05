from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

comb = combinations(card, 3)

result = []
for i in comb:
    if sum(i) <= m:
        result.append(sum(i))

result.sort()
print(result[-1])
