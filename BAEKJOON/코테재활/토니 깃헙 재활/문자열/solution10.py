temp = input()
s = ''
for i in temp:
    if i.isalpha():
        s += i

k = input()
print(1 if k in s else 0)
