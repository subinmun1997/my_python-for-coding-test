l, r = map(str, input().split())
Llen, Rlen = len(l), len(r)

count = 0
if Llen != Rlen:
    print(count)

else:
    for i in range(Llen):
        if l[i] != r[i]:
            break
        else:
            if l[i] == '8':
                count += 1

    print(count)