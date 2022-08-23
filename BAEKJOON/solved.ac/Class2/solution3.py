n = int(input())

word = set()
for _ in range(n):
    word.add(input())

word = sorted(word, key=lambda x : (len(x), x))
for i in word:
    print(i)