import itertools

x = input()
number = list(map(str, x))

perm = itertools.permutations(number, len(x))
result = []
for i in list(perm):
    temp = ''
    for j in i:
        temp += j
    result.append(int(temp))

check = [i for i in result if i > int(x)]
check.sort()

if len(check) != 0:
    print(check[0])
else:
    print(0)