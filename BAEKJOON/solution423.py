alphabet = [chr(i) for i in range(65, 91)]

t = int(input())
for _ in range(t):
    s = input()
    not_exists = []
    for a in alphabet:
        if a not in s:
            not_exists.append(ord(a))

    print(sum(not_exists))