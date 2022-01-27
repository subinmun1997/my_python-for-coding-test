t = int(input())

for _ in range(t):
    op = input().split()
    num = float(op.pop(0))
    for i in op:
        if i == '@':
            num *= 3
        elif i == '%':
            num += 5
        else:
            num -= 7
    result = "{:.2f}".format(num)
    print(result)