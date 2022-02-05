string = input()
s_list = string.split(' ')

basic_type = s_list.pop(0) # 기본 변수형

for s in s_list:
    s = s.replace(',', '')
    s = s.replace(';', '')

    print(basic_type, end='')

    for i in range(len(s)-1, 0, -1):
        if not s[i].isalpha():
            if s[i] == ']':
                print('[', end='')
            elif s[i] == '[':
                print(']', end='')
            else:
                print(s[i], end='')

    print(' ', end='')
    for i in range(len(s)):
        if s[i].isalpha():
            print(s[i], end='')

    print(';')