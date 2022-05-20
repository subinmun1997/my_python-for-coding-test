v = ('a', 'i', 'y', 'e', 'o', 'u')
V = ('A', 'I', 'Y', 'E', 'O', 'U')
c = ('b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f')
C = ('B', 'K', 'X', 'Z', 'N', 'H', 'D', 'C', 'W', 'G', 'P', 'V', 'J', 'Q', 'T', 'S', 'R', 'L', 'M', 'F')


while True:
    try:
        S = input()
        result = ''
        for s in S:
            if s in v:
                result += v[(v.index(s) + 3) % 6]
            elif s in V:
                result += V[(V.index(s) + 3) % 6]
            elif s in c:
                result += c[(c.index(s) + 10) % 20]
            elif s in C:
                result += C[(C.index(s) + 10) % 20]
            else:
                result += s
        print(result)
    except EOFError:
        break