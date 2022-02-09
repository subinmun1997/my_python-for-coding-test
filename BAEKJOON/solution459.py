sign = {
    '-':0,
    '\\':1,
    '(':2,
    '@':3,
    '?':4,
    '>':5,
    '&':6,
    '%':7,
    '/':-1
}

while True:
    n = input()
    if n == "#":
        break

    exp = len(n)-1
    answer = 0
    for i in n:
        answer += (sign[i] * (8**exp))
        exp -= 1

    print(answer)
