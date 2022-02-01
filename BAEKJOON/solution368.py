alpha = dict()
for i in range(1, 27):
    alpha[str(chr(65+i-1))] = i

def alpha_distance(a, b):
    x, y = alpha[a], alpha[b]
    if y >= x:
        return y-x
    else:
        return y+26-x

count = int(input())
for _ in range(count):
    a, b = map(str, input().split())
    a, b = list(a), list(b)
    print('Distances: ', end='')
    for i in range(len(a)):
        print(alpha_distance(a[i], b[i]), end=' ')
    print()