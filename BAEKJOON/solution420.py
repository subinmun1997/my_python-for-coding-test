while True:
    word = input()
    if word == "#":
        break
    check = word[0]
    word = word[1:].lower()

    print(check, word.count(check))