t = int(input())
for _ in range(t):
    pw = input()

    left = []
    right = []
    for p in pw:
        if p.isalnum():
            left.append(p)
        elif p == '<':
            if left:
                right.append(left.pop())
        elif p == '>':
            if right:
                left.append(right.pop())
        elif p == '-':
            if left:
                left.pop()

    print(''.join(left) + ''.join(reversed(right)))