n = int(input())

passwords = []
for _ in range(n):
    passwords.append(input())

for password in passwords:
    if password[::-1] in passwords:
        print(len(password), password[len(password)//2])
        break