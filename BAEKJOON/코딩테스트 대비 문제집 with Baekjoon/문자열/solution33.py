alpha = ["c=", "c-", "d-", "s=", "z=", "dz=", "lj", "nj"]
s = input()

count = 0
for i in alpha:
    if i in s:
        count += s.count(i)
        s = s.replace(i, 'X')

remain = 0
for i in s:
    if i != 'X':
        remain += 1

print(count+remain)

