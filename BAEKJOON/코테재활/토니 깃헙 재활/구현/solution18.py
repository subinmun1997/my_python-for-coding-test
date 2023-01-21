word = list(input())

idx = 0
start = 0

while idx < len(word):
    if word[idx] == '<':
        while word[idx] != '>':
            idx += 1
        idx += 1
    elif word[idx].isalnum():
        start = idx
        while idx < len(word) and word[idx].isalnum():
            idx += 1
        temp = word[start:idx]
        temp.reverse()
        word[start:idx] = temp
    else:
        idx += 1

print(''.join(word))