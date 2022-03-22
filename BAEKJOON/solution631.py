t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    book = [i for i in range(1, n + 1)]
    reserve = [list(map(int, input().split())) for _ in range(m)]
    reserve.sort(key=lambda x : x[1])

    student = 0
    for a, b in reserve:
        for i in range(a, b+1):
            if i in book:
                book.pop(book.index(i))
                student += 1
                break

    print(student)