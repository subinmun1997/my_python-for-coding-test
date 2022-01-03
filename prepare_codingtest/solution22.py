s = input()

alpha = []
digits = 0

for i in s:
    if i.isalpha():
        alpha.append(i)
    else:
        digits += int(i)

alpha.sort()
alpha.append(str(digits))

print(''.join(alpha))