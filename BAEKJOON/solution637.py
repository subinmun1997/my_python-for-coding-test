word = input()
if word == 'P' or word == 'PPAP':
    print('PPAP')
else:
    stack = []
    ppap = ['P','P','A','P']
    for i in word:
        stack.append(i)
        if stack[-4:] == ppap:
            stack.pop()
            stack.pop()
            stack.pop()

    if stack == ppap or stack == ['P']:
        print('PPAP')
    else:
        print('NP')