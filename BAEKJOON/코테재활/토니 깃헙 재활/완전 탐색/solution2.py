from itertools import permutations

n, m = map(int, input().split())
card = list(map(int, input().split()))

result = []
for i in permutations(card, 3):
    if sum(i) <= m:
        result.append(sum(i))

result.sort(reverse=True)
print(result[0])