max_len = 0
words = []
for _ in range(5):
    s = list(input())
    max_len = max(max_len, len(s))
    words.append(s)

for word in words:
    for i in range(max_len - len(word)):
        word.append('-')

result = ''
for i in range(max_len):
    for j in range(5):
        if words[j][i] != '-':
            result += words[j][i]

print(result)