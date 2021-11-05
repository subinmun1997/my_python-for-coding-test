n = int(input())
words = set()

for i in range(n):
    words.add(input())

words = list(words)
words_sort = sorted(words, key=lambda x:(len(x),x))

for i in words_sort:
    print(i)