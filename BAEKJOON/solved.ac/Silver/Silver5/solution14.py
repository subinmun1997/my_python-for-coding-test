n = int(input())
words = set(input() for _ in range(n))

words = sorted(words, key=lambda x : (len(x), x))
for word in words:
    print(word)