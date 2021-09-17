s = input()

number = 0
alpha = []

for i in s:
    if i.isdigit():
        number += int(i)
    else:
        alpha.append(i)

alpha.sort()
alpha.append(str(number))
print(''.join(alpha))