s = input()
for i in s:
    print(i.lower() if i.isupper() else i.upper(), end='')