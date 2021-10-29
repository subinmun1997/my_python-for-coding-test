E, S, M = map(int, input().split())

def year(E, S, M):
    e, s, m = 1, 1, 1
    for i in range(15*28*19):
        if e == E and s == S and m == M:
            return i+1
        e = e + 1 if e < 15 else 1
        s = s + 1 if s < 28 else 1
        m = m + 1 if m < 19 else 1

result = year(E, S, M)
print(result)
