while True:
    n = input()
    if n == '0':
        break

    while len(n) != 1:
        n = str(sum(list(map(int, n))))
    print(n)