s = input()

for i in s:
    if i.islower():
        i = i.upper()
        print(i, end='')
    elif i.isupper():
        i = i.lower()
        print(i, end='')