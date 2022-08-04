n = input()
n = int(''.join(sorted(n, reverse=True)))
print(n if n%30 == 0 else -1)
