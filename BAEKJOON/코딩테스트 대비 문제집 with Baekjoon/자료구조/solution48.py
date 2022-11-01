n = int(input())

for _ in range(n):
    left = []
    right = []
    word = input()

    for w in word:
        if w == "<":
            if left:
                right.append(left.pop())
        elif w == ">":
            if right:
                left.append(right.pop())
        elif w == "-":
            if left:
                left.pop()
        else:
            left.append(w)

    print("".join(left) + "".join(reversed(right)))