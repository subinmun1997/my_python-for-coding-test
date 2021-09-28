a = []
for i in range(10):
    a.append(int(input()))

div = []
for i in a:
    div.append(i%42)

div = set(div)
print(len(div))