from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = []
for comb in combinations(cards, 3):
    if sum(comb) <= m:
        result.append(sum(comb))

result.sort()
print(result[-1])