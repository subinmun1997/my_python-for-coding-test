word1 = list(input())
word2 = list(input())

i = 0
while i < len(word1):
    if word1[i] in word2:
        word2.remove(word1[i])
        word1.remove(word1[i])
        i -= 1
    i += 1

print(len(word1) + len(word2))