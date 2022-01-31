import itertools

seven = [int(input()) for _ in range(9)]
check = list(itertools.combinations(seven, 7))

for i in check:
    if sum(i) == 100:
        answer = sorted(i)

for i in answer:
    print(i)