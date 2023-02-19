from collections import Counter

n = int(input())
for _ in range(n):
    word = input().replace(' ', '')
    counter = Counter(word).most_common(2)

    if len(counter) == 1:
        print(counter[0][0])
    else:
        print(counter[0][0] if counter[0][1] != counter[1][1] else '?')