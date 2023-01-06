from itertools import combinations

data = input()

ps = []
temp = []
for idx, k in enumerate(data):
    if k == '(':
        temp.append(idx)
    elif k == ')':
        ps.append((temp.pop(), idx))

answer = set()
for i in range(1, len(ps)+1):
    comb = combinations(ps, i)
    for c in comb:
        _data = list(data)
        for x, y in c:
            _data[x] = ''
            _data[y] = ''
            answer.add(''.join(_data))

for i in sorted(answer):
    print(i)