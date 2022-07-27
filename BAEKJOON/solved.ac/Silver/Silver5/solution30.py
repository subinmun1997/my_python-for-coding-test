import sys
input = sys.stdin.readline

s = set()
n = int(input())
for _ in range(n):
    data = input().split()

    if len(data) == 2:
        x = int(data[1])

    if data[0] == 'add':
        s.add(x)
    elif data[0] == 'remove':
        s.discard(x)
    elif data[0] == 'check':
        if x in s:
            print(1)
        else:
            print(0)
    elif data[0] == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif data[0] == 'all':
        s = set([i for i in range(1, 21)])
    elif data[0] == 'empty':
        s = set([])