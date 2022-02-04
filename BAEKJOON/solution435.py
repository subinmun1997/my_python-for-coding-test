number = ['0','1','2','3','4','5','6','7','8','9']

n = int(input())
words = input()

hidden = ''
result = []

for word in words:
    if word in number:
        hidden += word
    else:
        result.append(hidden)
        hidden = ''
result.append(hidden)

total = 0
for r in result:
    if r == '':
        continue
    else:
        total += int(r)

print(total)