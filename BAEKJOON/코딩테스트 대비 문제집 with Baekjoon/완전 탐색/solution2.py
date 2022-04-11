from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

array = list(combinations(cards, 3))
result = []
for i in array:
    if sum(i) <= m:
        result.append(i)
result.sort(key=lambda x : sum(x))
print(sum(result[-1]))