s = input()
joi = ioi = 0

for i in range(len(s)-2):
    answer = s[i:i+3]

    if answer == 'JOI':
        joi += 1
    if answer == 'IOI':
        ioi += 1

print(joi)
print(ioi)