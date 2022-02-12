n = int(input())
name = {}
for _ in range(n):
    x = input()
    if x[0] in name:
        name[x[0]] += 1
    else:
        name[x[0]] = 1

dict_values = list(name.values())
if max(dict_values) < 5:
    print("PREDAJA")


for k, v in sorted(name.items()):
    if v >= 5:
        print(k, end='')