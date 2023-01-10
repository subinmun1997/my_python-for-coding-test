import sys
input = sys.stdin.readline

n, m = map(int, input().split())

name = []
pocketmon_dict = dict()
for i in range(1, n+1):
    n = input().strip()
    name.append(n)
    pocketmon_dict[i] = n

for _ in range(m):
    find = input().strip()
    if find.isalpha():
        print(name.index(find)+1)
    else:
        print(pocketmon_dict[int(find)])