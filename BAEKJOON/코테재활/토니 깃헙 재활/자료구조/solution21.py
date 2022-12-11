t = int(input())
for _ in range(t):
    pw = input()
    lstack = []
    rstack = []

    for i in pw:
        if i == '<' and lstack:
            rstack.append(lstack.pop())
        elif i == '>' and rstack:
            lstack.append(rstack.pop())
        elif i == '-':
            if lstack:
                lstack.pop()
        elif i.isalnum():
            lstack.append(i)

    print(''.join(lstack) + ''.join(reversed(rstack)))



