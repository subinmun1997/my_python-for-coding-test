n = int(input())
name_dict = {}

for _ in range(n):
    x = input()
    if x[0] in name_dict:
        name_dict[x[0]] += 1
    else:
        name_dict[x[0]] = 1

values = name_dict.values()
if max(values) < 5:
    print("PREDAJA")

for k, v in sorted(name_dict.items()):
    if v >= 5:
        print(k, end='')