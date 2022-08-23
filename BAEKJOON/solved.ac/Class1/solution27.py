word = input()

for i in range(97, 123):
    if chr(i) in word:
        print(word.index(chr(i)), end=' ')
    else:
        print(-1, end=' ')