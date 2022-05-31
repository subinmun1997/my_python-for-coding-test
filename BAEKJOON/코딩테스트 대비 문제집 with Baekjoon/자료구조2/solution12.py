n = int(input())
book = {}

for _ in range(n):
    name = input()
    if name in book:
        book[name] += 1
    else:
        book[name] = 1

answer = sorted(book.items(), key=lambda x : (-x[1], x[0]))
print(answer[0][0])

