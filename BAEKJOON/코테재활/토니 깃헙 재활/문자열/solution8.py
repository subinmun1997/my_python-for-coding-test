n = int(input())
word = set(input() for _ in range(n))
word = sorted(word, key=lambda x:(len(x), x))

for i in word:
    print(i)