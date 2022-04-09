s = input()
k = input()

result = ''
for i in s:
    if i.isalpha():
        result += i

print(1 if k in result else 0)