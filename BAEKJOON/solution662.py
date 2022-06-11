num = 1
while True:
    a = input()
    b = input()
    if a == 'END' and b == 'END':
        break

    if sorted(a) == sorted(b):
        print(f"Case {num}: same")
    else:
        print(f"Case {num}: different")
    num += 1