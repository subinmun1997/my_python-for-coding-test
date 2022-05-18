n = int(input())
pw = [input() for _ in range(n)]

for i in pw:
    if i[::-1] in pw:
        print(len(i), i[len(i)//2])
        break
