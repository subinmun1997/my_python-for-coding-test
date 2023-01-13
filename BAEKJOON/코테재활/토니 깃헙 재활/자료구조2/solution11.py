n = int(input())

book = dict()
for _ in range(n):
    name = input()
    if name in book:
        book[name] += 1
    else:
        book[name] = 1

book = sorted(book.items(), key=lambda x : (-x[1], x[0]))
print(book[0][0])