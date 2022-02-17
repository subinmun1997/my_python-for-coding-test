chemistry = input()

dic = {
    'H':1,
    'C':12,
    'O':16
}

stack = []

for c in chemistry:
    if c in dic:
        stack.append(dic[c])
    elif c == '(':
        stack.append(c)
    elif c == ')':
        temp = 0
        while True:
            p = stack.pop()
            if p == '(':
                break
            temp += p
        if temp == 0:
            continue
        else:
            stack.append(temp)
    else:
        n = stack.pop()
        temp = n * int(c)
        stack.append(temp)

print(sum(stack))