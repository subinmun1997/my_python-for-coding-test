from itertools import combinations

s = input()

lst = []
stack = []
result = set()

for idx, v in enumerate(s):
    if v == '(':
        stack.append(idx)
    elif v == ')':
        start = stack.pop()
        end = idx
        lst.append((start, end))

for i in range(1, len(lst)+1):
    comb = combinations(lst, i)
    for j in comb:
        temp = list(s)
        for k in j:
            start, end = k
            temp[start] = ''
            temp[end] = ''
        result.add(''.join(temp))

for i in sorted(result):
    print(i)
