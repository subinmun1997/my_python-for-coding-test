while True:
    n = int(input())
    if n == 0:
        break

    words = []
    for _ in range(n):
        words.append(input())
    words = sorted(words, key=lambda word : word.lower())
    print(words[0])