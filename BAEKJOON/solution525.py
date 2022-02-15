s = input()

number = []
for i in s:
    if i.isdigit():
        number.append(i)
    elif i == '+':
        a = number.pop()
        b = number.pop()
        number.append(int(a)+int(b))
    elif i == '-':
        a = number.pop()
        b = number.pop()
        number.append(int(b) - int(a))
    elif i == '*':
        a = number.pop()
        b = number.pop()
        number.append(int(a) * int(b))
    else:
        a = number.pop()
        b = number.pop()
        number.append(int(b) // int(a))

print(number[0])