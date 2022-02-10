n = int(input())

for _ in range(n):
    name = input()
    name_lower = name.lower()
    if name_lower.count('g') > name_lower.count('b'):
        print(name, "is GOOD")
    elif name_lower.count('g') < name_lower.count('b'):
        print(name, "is A BADDY")
    else:
        print(name, "is NEUTRAL")