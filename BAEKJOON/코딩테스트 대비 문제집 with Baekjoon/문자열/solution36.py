while True:
    n = int(input())
    if n == 0:
        break

    words = [input() for _ in range(n)]
    words = sorted(words, key=lambda x : x.lower())
    print(words[0])