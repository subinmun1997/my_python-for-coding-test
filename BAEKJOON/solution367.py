n = int(input())

alphabet = {
    'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,
    'F':6,
    'G':7,
    'H':8,
    'I':9,
    'J':10,
    'K':11,
    'L':12,
    'M':13,
    'N':14,
    'O':15,
    'P':16,
    'Q':17,
    'R':18,
    'S':19,
    'T':20,
    'U':21,
    'V':22,
    'W':23,
    'X':24,
    'Y':25,
    'Z':26
}

array = []
for _ in range(n):
    x, y = map(str, input().split())
    array.append((x, y))


for x, y in array:
    distance = []
    for i in range(len(x)):
        if alphabet[x[i]] <= alphabet[y[i]]:
            distance.append(alphabet[y[i]]-alphabet[x[i]])
        else:
            distance.append(alphabet[y[i]]+26-alphabet[x[i]])
    print("Distances:", end=' ')
    for i in distance:
        print(i, end=' ')
    print()