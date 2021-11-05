import itertools

arr = [int(input()) for _ in range(9)]
c = list(itertools.combinations(arr,7))


for i in c:
    if sum(i) == 100:
        answer = sorted(i)

for i in answer:
    print(i)