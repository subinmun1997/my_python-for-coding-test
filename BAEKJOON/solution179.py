while True:
    try:
        low, upp, digit, space = 0, 0, 0, 0
        for i in input():
            if i.islower():
                low += 1
            elif i.isupper():
                upp += 1
            elif i.isdigit():
                digit += 1
            else:
                space += 1
        print(low, upp, digit, space)
    except EOFError:
        break
