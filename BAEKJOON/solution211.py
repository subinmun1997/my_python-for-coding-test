n = input()
arr = list(map(int, n))
b = sum(arr)

if b%3==0:
    arr.sort(reverse=True)
    c = arr[-1]
    if c==0:
        a = ''.join(map(str,arr))
        a = int(a)
        print(a)
    else:
        print(-1)
else:
    print(-1)