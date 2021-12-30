n = int(input())

words = []
for _ in range(n):
    words.append(input())

dict = {}
for word in words:
    root = len(word) - 1
    for c in word:
        if c in dict:
            dict[c] += pow(10, root)
        else:
            dict[c] = pow(10, root)
        root -= 1

dict = sorted(dict.values(), reverse=True)

result, m = 0, 9
for value in dict:
    result += value * m
    m -= 1

print(result)