t = int(input())
for _ in range(t):
    n = int(input())
    alphabet = list(map(str, input().split()))

    answer = []
    answer.append(alphabet[0])
    for i in range(1, len(alphabet)):
        if int(ord(alphabet[i])) <= int(ord(answer[0])):
            answer.insert(0, alphabet[i])
        else:
            answer.append(alphabet[i])

    print(''.join(answer))
