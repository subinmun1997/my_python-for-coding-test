mbti = input()

ideal = ''
for m in mbti:
    if m == 'E':
        ideal += 'I'
    elif m == 'I':
        ideal += 'E'
    elif m == 'S':
        ideal += 'N'
    elif m == 'N':
        ideal += 'S'
    elif m == 'T':
        ideal += 'F'
    elif m == 'F':
        ideal += 'T'
    elif m == 'J':
        ideal += 'P'
    elif m == 'P':
        ideal += 'J'

print(ideal)