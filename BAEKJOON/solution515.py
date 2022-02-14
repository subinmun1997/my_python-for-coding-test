t = int(input())

for _ in range(t):
    word = input()
    ruls = input()

    for w in word:
        if w == " ":
            print(" ", end='')
        else:
            print(ruls[int(ord(w)) - int(ord('A'))], end='')
    print()
