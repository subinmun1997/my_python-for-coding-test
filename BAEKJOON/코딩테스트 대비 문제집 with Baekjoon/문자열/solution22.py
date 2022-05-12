s = input()
alpha = []
for i in range(97, 123):
    alpha.append(chr(i))

for a in alpha:
    print(s.index(a) if a in s else -1, end=' ')