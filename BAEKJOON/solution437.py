def rev(a, b, c):
    a = a[::-1]
    b = b[::-1]
    c = c[::-1]

    rev_word = a+b+c
    return rev_word

s = input()
word_list = []

for i in range(1,len(s)-1):
    for j in range(i+1, len(s)):
        a, b, c = s[:i], s[i:j], s[j:]
        word_list.append(rev(a, b, c))

word_list.sort()
print(word_list[0])