n = int(input())
for _ in range(n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha = list(alpha)
    word = input().lower()
    for i in word:
        if i in alpha:
            alpha.remove(i)

    print("pangram" if not alpha else "missing " + ''.join(alpha))
