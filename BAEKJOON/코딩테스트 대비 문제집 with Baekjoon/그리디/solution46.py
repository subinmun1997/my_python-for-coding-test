a = input()
b = input()

answer = 0
if sorted(a) != sorted(b):
    print(-1)
else:
    cur = len(a) - 1
    for i in range(len(a)-1, -1, -1):
        if a[i] != b[cur]:
            answer += 1
        else:
            cur -= 1

    print(answer)