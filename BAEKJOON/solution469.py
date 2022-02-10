r, c, zr, zc = map(int, input().split())
newspaper = [input() for _ in range(r)]

for i in range(r):
    for j in range(zr):
        for k in range(c):
            for m in range(zc):
                print(newspaper[i][k], end='')

        print()
