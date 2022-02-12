s = input()
k = input()

remove_digit = ''
for i in s:
    if i.isalpha():
        remove_digit += i

print(1 if k in remove_digit else 0)