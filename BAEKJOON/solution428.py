alphabet = [chr(i) for i in range(97, 123)]

while True:
    check = True
    words = input()
    if words == '*':
        break
    for a in alphabet:
        if a not in words:
            check = False
            break

    if check:
        print("Y")
    else:
        print("N")

