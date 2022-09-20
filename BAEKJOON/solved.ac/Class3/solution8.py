n, m = map(int, input().split())

pocketmon_name = []
pocketmon_dict = {}
for i in range(1, n+1):
    name = input()
    pocketmon_name.append(name)
    pocketmon_dict[name] = i

for _ in range(m):
    v = input()
    if v.isdigit():
        print(pocketmon_name[int(v)-1])
    else:
        print(pocketmon_dict[v])
