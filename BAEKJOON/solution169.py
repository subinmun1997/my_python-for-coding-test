import itertools

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(i+1)

result = itertools.combinations(array, m)

for i in result:
    for j in i:
        print(j, end=' ')
    print()