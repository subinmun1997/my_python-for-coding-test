t = int(input())

for _ in range(t):
    n, word = map(str, input().split())
    for i in word:
        print(i * int(n), end='')
    print()