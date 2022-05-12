word = input()
key = input()

answer = ''
for i in range(len(word)):
    if word[i] == ' ':
        answer += ' '
        continue
    diff = ord(word[i]) - ord(key[i%len(key)])
    if diff > 0:
        answer += chr(diff+96)
    else:
        answer += chr(diff+26+96)

print(answer)

