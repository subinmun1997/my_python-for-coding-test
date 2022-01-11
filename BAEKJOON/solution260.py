n = int(input())

names = []
for _ in range(n):
    names.append(input())

inc = sorted(names)
dec = sorted(names, reverse=True)

if names == inc:
    print("INCREASING")
elif names == dec:
    print("DECREASING")
else:
    print("NEITHER")
