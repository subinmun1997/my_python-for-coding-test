n = input()
if '0x' in n:
    print(int(n[2:], 16))
elif n[0] == '0':
    print(int(n[1:], 8))
else:
    print(n)