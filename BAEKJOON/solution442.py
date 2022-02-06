find_word = input()
n = int(input())

count = 0
for _ in range(n):
    word = input()

    check = word+word
    if find_word in check:
        count += 1

print(count)