import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pocketmon_names = []
pocketmon_list = {}

for i in range(1, n+1):
    x = input().rstrip()
    pocketmon_names.append(x)
    pocketmon_list[x] = i

for i in range(m):
    x = input().rstrip()

    if x.isdigit():
        print(pocketmon_names[int(x)-1])
    else:
        print(pocketmon_list[x])