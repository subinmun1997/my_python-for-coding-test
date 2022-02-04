s = input()

if ':-)' in s or ':-(' in s:
    happy = s.count(')')
    sad = s.count('(')

    if happy == sad:
        print("unsure")
    elif happy > sad:
        print("happy")
    else:
        print("sad")

else:
    print("none")