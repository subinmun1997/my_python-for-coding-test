import itertools

n = int(input())

max_num = 0
idx = 0

for i in range(n):
    data = list(map(int, input().split()))
    comb = list(itertools.combinations(data, 3))
    for j in range(len(comb)):
        comb[j] = sum(comb[j])%10

    if max_num <= max(comb):
        max_num = max(comb)
        idx = i+1

print(idx)
