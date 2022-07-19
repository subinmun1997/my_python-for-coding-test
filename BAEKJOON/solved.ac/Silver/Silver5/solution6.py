def d():
    not_make = []
    for i in range(1, 10001):
        a = list(map(int, str(i)))
        temp = i + sum(a)

        if temp not in not_make and temp <= 10000:
            not_make.append(temp)

    for p in range(1, 10001):
        if p not in not_make:
            print(p)

d()