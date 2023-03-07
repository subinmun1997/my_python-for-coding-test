n, m = map(int, input().split())
dna = [list(input()) for _ in range(n)]

result = ''
hd = 0
for j in range(m):
    a, c, g, t = 0, 0, 0, 0
    for i in range(n):
        if dna[i][j] == 'A':
            a += 1
        elif dna[i][j] == 'C':
            c += 1
        elif dna[i][j] == 'G':
            g += 1
        elif dna[i][j] == 'T':
            t += 1

    if max(a, c, g, t) == a:
        result += 'A'
        hd += c + g + t
    elif max(a, c, g, t) == c:
        result += 'C'
        hd += a + g + t
    elif max(a, c, g, t) == g:
        result += 'G'
        hd += a + c + t
    elif max(a, c, g, t) == t:
        result += 'T'
        hd += a + c + g

print(result)
print(hd)
