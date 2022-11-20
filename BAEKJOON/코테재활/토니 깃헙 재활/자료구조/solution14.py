from itertools import combinations

data = input()
ps = []
stack = []
result = set()

for x, y in enumerate(data):
    if y == '(':
        stack.append(x)
    elif y == ')':
        start = stack.pop()
        ps.append((start, x))

for i in range(1, len(ps)+1):
    comb = combinations(ps, i)
    for c in comb:
        temp = list(data)
        for k in c:
            start, end = k
            temp[start] = ''
            temp[end] = ''
        result.add(''.join(temp))

for i in sorted(result):
    print(i)