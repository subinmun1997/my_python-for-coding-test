while True:
    x = input()
    if x == '0':
        break
    print("yes" if x == x[::-1] else "no")