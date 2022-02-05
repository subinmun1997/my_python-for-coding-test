while True:
    n = int(input())
    if n == 0:
        break

    dict = {}
    for _ in range(n):
        word = input()
        dict[word] = word.lower()

    dict = sorted(dict.items(), key=lambda x : x[1])
    print(dict[0][0])