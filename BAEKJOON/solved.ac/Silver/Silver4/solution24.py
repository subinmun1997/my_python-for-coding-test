n, m = map(int, input().split())

nick_name = []
name_dict = {}
for i in range(1, n+1):
    pocketmon = input()
    nick_name.append(pocketmon)
    name_dict[pocketmon] = i

for _ in range(m):
    data = input()
    if data.isdigit():
        print(nick_name[int(data)-1])
    else:
        print(name_dict[data])