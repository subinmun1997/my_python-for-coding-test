alphabet = {}
for i in range(97, 123):
    alphabet[chr(i)] = i - 96

for i in range(65,91):
    alphabet[chr(i)] = i - 38

def check_sosu(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

n = input()
count = 0
for i in n:
    count += alphabet[i]
if check_sosu(count):
    print("It is a prime word.")
else:
    print("It is not a prime word.")