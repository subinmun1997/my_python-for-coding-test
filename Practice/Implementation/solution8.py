s = input()
total = 0
array_alpha = []

for i in s:
    if i.isalpha():
        array_alpha.append(i)
    else:
        total += int(i)

array_alpha.sort()

for i in array_alpha:
    print(i, end='')
print(total)