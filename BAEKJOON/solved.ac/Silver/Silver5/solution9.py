n = int(input())
count = 0

for _ in range(n):
    word = input()
    a = '0'
    check = []

    for w in word:
        if w != a:
            check.append(w)
        a = w
    if len(check) == len(set(check)):
        count += 1

print(count)